
from .views import job_list, job_detail
from .views import ResumeCreateView
from django.urls import path, re_path

urlpatterns = [
    path('', job_list, name='jobs-index'),
    path('joblist/', job_list, name='job-list'),
    path('<int:job_id>/', job_detail, name='job-detail'),
]
