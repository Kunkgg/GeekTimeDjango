from .job import job_list, job_detail
from .resume import ResumeDetailView, ResumeCreateView
from .api import UserViewSet, JobViewSet, ResumeViewSet
from .demo_hack import detail_resume_xss, create_hr_user_csrf