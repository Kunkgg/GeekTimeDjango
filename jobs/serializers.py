from django.contrib.auth.models import User

from rest_framework import serializers

from jobs.models import Job, Resume


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
        extra_kwargs = {
            'url': {'view_name': 'api-users-detail'},
        }


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
        extra_kwargs = {
            'url': {'view_name': 'api-jobs-detail'},
        }

class ResumeSerializer(serializers.HyperlinkedModelSerializer):
    applicant = serializers.ReadOnlyField(source='applicant.username')
    created_date = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Resume
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'api-resumes-detail'},
        }