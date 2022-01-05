"""recruitment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from jobs import views as jobs_views

admin.site.site_header = '匠果科技招聘系统'
admin.site.site_title = '匠果科技招聘系统'

urlpatterns = [
    path('', jobs_views.job_list),
    path('resume/add/', jobs_views.ResumeCreateView.as_view(), name='resume_add'),
    path('resume/<int:pk>/', jobs_views.ResumeDetailView.as_view(), name='resume_detail'),
    path('grappelli/', include('grappelli.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
    path('jobs/', include('jobs.urls'), name='jobs'),
]
