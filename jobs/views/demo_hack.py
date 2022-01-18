import logging

from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt

from jobs.models import Resume

LOG = logging.getLogger()

# ---------------------------------------------------------------------------
#   Demo for web hack
# ---------------------------------------------------------------------------
#region
def detail_resume_xss(request, pk):
    '''demo for XSS

    @retrun HTML content without escape
    trigger xss:
    <script>alert('page cookies:\n' + document.cookie);</script>
    '''
    try:
        resume = Resume.objects.get(pk=pk)
        content = f'name: {resume.username} <br> introduction: {resume.candidate_introduction} <br>'
        return HttpResponse(content)
    except Resume.DoesNotExist:
        raise Http404('resume does not exist')


@csrf_exempt
@permission_required('auth.user_add')
def create_hr_user_csrf(request):
    '''demo for CSRF

    @retrun HTML form without crsf_token
    '''
    hr_group_name = 'HR'
    template_name = 'create_hr_csrf.html'
    # messages.info(request, f'hi, {request.user.username}')
    if request.method == 'GET':
        return render(request, template_name, {})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_set = User.objects.filter(username=username)
        if len(user_set) > 0:
            msg = f'Failed, username: {username} is already existed.'
            LOG.warning(msg)
            messages.warning(request, msg)
        else:
            hr_group = Group.objects.get(name=hr_group_name) 
            user = User(is_superuser=False, username=username, is_active=True, is_staff=True)
            user.set_password(password)
            user.save()
            user.groups.add(hr_group)
            msg = f'Successed, created {username}.'
            LOG.info(msg)
            messages.info(request, msg)
        return render(request, template_name)
    return render(request, template_name)
#endregion