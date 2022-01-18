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
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseServerError
from django.views.generic.base import RedirectView
from rest_framework import routers
from jobs import views as jobs_views
from interview import views as interview_views


admin.site.site_header = _('匠果科技招聘系统')
admin.site.site_title = _('匠果科技招聘系统')

#pylint: disable=unused-variable
def trigger_error(request):
    division_by_zero = 1 / 0
    return HttpResponseServerError()
#pylint: enable=unused-variable

# ---------------------------------------------------------------------------
#   REST Framework
# ---------------------------------------------------------------------------
#region
router = routers.DefaultRouter()
router.register(r'users', jobs_views.UserViewSet, basename='api-users')
router.register(r'jobs', jobs_views.JobViewSet, basename='api-jobs')
router.register(r'candidate', interview_views.CandidateViewSet, basename='api-candidate')
router.register(r'resumes', jobs_views.ResumeViewSet, basename='api-resumes')

urlpatterns_rest_framework = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
#endregion


urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('', jobs_views.job_list),
    # path('', RedirectView.as_view(pattern_name='jobs-index', permanent=False), name='home'),
    path('jobs/', include('jobs.urls'), name='jobs'),
    path('resume/add/', jobs_views.ResumeCreateView.as_view(), name='resume-add'),
    path('resume/<int:pk>/', jobs_views.ResumeDetailView.as_view(), name='resume-detail'),
    path('resume_xss/<int:pk>/', jobs_views.detail_resume_xss, name='resume-detail-xss'),
    path('create_hr_user_csrf/', jobs_views.create_hr_user_csrf, name='create-hr-user-csrf'),
    # try sentry
    path('sentry-debug/', trigger_error),
]

urlpatterns += urlpatterns_rest_framework
