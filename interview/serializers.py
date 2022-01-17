from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    # creator = serializers.ReadOnlyField(source='creator.username')
    creator = serializers.ReadOnlyField(source='creator.username')
    created_date = serializers.DateTimeField(read_only=True)
    modified_date = serializers.DateTimeField(read_only=True)
    last_editor = serializers.CharField(read_only=True)
    class Meta:
        model = Candidate
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'api-candidate-detail'},
            'first_interviewer_user': {'view_name': 'api-users-detail'},
            'second_interviewer_user': {'view_name': 'api-users-detail'},
            'hr_interviewer_user': {'view_name': 'api-users-detail'},
        }