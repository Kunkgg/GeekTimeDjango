from django.shortcuts import render
from rest_framework import viewsets

from .models import Candidate
from .serializers import CandidateSerializer

# Create your views here.

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer