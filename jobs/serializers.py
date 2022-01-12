from django.contrib.auth.models import User
from django.utils import timezone

from rest_framework import serializers

from .models import Job, Resume


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class JobSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    created_date = serializers.DateTimeField(read_only=True)
    modified_date = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Job
        fields = [
            'url',
            'creator',
            'job_type',
            'job_name',
            'job_city',
            'job_responsibility',
            'job_requirement',
            'created_date',
            'modified_date',
        ]

class ResumeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'
