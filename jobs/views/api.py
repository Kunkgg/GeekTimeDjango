from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils import timezone
from django.db.models import Q
from django.urls import reverse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action

from jobs.models import Job, Resume
from jobs.serializers import UserSerializer, JobSerializer, ResumeSerializer
from jobs.permissions import IsHROrReadOnly, IsUserSelf
from interview.models import Candidate

# ---------------------------------------------------------------------------
#   REST framework
# ---------------------------------------------------------------------------
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserSelf]


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsHROrReadOnly]

    def perform_create(self, serializer):
        serializer.save(
            creator=self.request.user,
            created_date=timezone.now(),
            modified_date=timezone.now())

    def perform_update(self, serializer):
        serializer.save(modified_date=timezone.now())


class ResumeViewSet(viewsets.ModelViewSet):
    # queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        qs = Resume.objects.none()
        user = self.request.user
        group_names = [group.name for group in user.groups.all()]
        if user.is_superuser or 'HR' in group_names:
            qs = Resume.objects.all()
        elif 'Interviewer' in group_names:
            qs = Resume.objects.all()
            candidates = Candidate.objects.filter(
                Q(first_interviewer_user=user) | Q(second_interviewer_user=user)
            )
            candidates_phones = [candidate.phone for candidate in candidates]
            qs = Resume.objects.filter(phone__in=candidates_phones)
        else:
            qs = Resume.objects.filter(applicant=user.id)
        return qs

    def perform_create(self, serializer):
        serializer.save(
            applicant=self.request.user,
            created_date=timezone.now(),
            modified_date=timezone.now())

    def perform_update(self, serializer):
        serializer.save(
            applicant=self.request.user,
            modified_date=timezone.now())

    @action(detail=True, permission_classes=[IsHROrReadOnly])
    def enter_interview_process(self, request, *args, **kwargs):
        resume = self.get_object()
        candidate = Candidate()
        # 把 obj 对象中的所有属性拷贝到 candidate 对象中:
        candidate.__dict__.update(resume.__dict__)
        candidate.created_date = datetime.now()
        candidate.modified_date = datetime.now()
        candidate.creator = request.user.username
        candidate.save()
        return redirect(reverse('api-candidate-detail', kwargs={'pk': candidate.pk}))