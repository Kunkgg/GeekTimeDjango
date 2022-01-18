
from django.urls import path
from jobs.views import job_list, job_detail

urlpatterns = [
    path('', job_list, name='jobs-index'),
    path('joblist/', job_list, name='job-list'),
    path('<int:job_id>/', job_detail, name='job-detail'),
]
