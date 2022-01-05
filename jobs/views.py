import logging

from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


from .models import Job, Resume
from .models import JobTypes
from .models import Cities
from .forms import ResumeForm

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
        return HttpResponseRedirect(self.success_url)
