from django.utils import timezone
from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets
from rest_framework import permissions

from .models import Candidate
from .serializers import CandidateSerializer

# Create your views here.

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [permissions.IsAdminUser,]

    def get_queryset(self):
        qs = Candidate.objects.none()
        user = self.request.user
        group_names = [group.name for group in user.groups.all()]
        if user.is_superuser or 'HR' in group_names:
            qs = Candidate.objects.all()
        elif 'Interviewer' in group_names:
            qs = Candidate.objects.filter(
                Q(first_interviewer_user=user) | Q(second_interviewer_user=user)
            )

        return qs

    def perform_create(self, serializer):
        serializer.save(
            creator=self.request.user,
            created_date=timezone.now(),
            modified_date=timezone.now(),
            last_editor=self.request.user.get_username())

    def perform_update(self, serializer):
        serializer.save(
            last_editor=self.request.user.get_username(),
            modified_date=timezone.now())