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
from django.utils.translation import gettext_lazy as _


from jobs import views as jobs_views

admin.site.site_header = _('匠果科技招聘系统')
admin.site.site_title = _('匠果科技招聘系统')

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('', jobs_views.job_list),
    path('jobs/', include('jobs.urls'), name='jobs'),
    path('resume/add/', jobs_views.ResumeCreateView.as_view(), name='resume_add'),
    path('resume/<int:pk>/', jobs_views.ResumeDetailView.as_view(), name='resume_detail'),
    path('resume_xss/<int:pk>/', jobs_views.detail_resume_xss, name='resume_detail_xss'),
    # try sentry
    path('sentry-debug/', trigger_error),
]
