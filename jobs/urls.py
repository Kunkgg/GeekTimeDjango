
from .views import job_list, job_detail
from django.urls import path, re_path

urlpatterns = [
    path('', job_list, name='jobs_index'),
    path('joblist/', job_list, name='joblist'),
    path('<int:job_id>/', job_detail, name='job_detail'),
]
