import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group, User
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets

from .forms import ResumeForm
from .models import Cities, Job, JobTypes, Resume
from .serializers import UserSerializer, JobSerializer, ResumeSerializer

LOG = logging.getLogger()


def job_list(request):
    jobs = Job.objects.all()
    for job in jobs:
        job.job_type = JobTypes[job.job_type][1]
        job.job_city = Cities[job.job_city][1]
    context = {
        'jobs': jobs,
    }
    return render(request, 'jobs/job_list.html', context)


def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    job.job_type = JobTypes[job.job_type][1]
    job.job_city = Cities[job.job_city][1]
    context = {
        'job': job,
    }

    LOG.info(f"request method: {request.method}, path: {request.path}")
    return render(request, 'jobs/job_detail.html', context)


class ResumeDetailView(generic.detail.DetailView):
    model = Resume


class ResumeCreateView(LoginRequiredMixin, generic.edit.CreateView):
    """    简历职位页面  """
    template_name = 'resume_form.html'
    success_url = '/jobs/joblist/'
    model = Resume
    fields = ["username", "city", "phone",
        "email", "apply_position", "gender",
        "bachelor_school", "master_school", "major", "degree", 
        "candidate_introduction", "work_experience", "project_experience"]

    ### 从 URL 请求参数带入默认值
    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# ---------------------------------------------------------------------------
#   REST framework
# ---------------------------------------------------------------------------
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

# ---------------------------------------------------------------------------
#   Demo for web hack
# ---------------------------------------------------------------------------
#region
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt

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