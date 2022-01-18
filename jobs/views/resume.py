from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views import generic

from jobs.models import Resume


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
        for attr in self.request.GET:
            initial[attr] = self.request.GET[attr]
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
