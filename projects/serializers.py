from rest_framework import serializers
from projects.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class meta:
        model = Project
        fields = [
            'started',
            'finished',
            'title',
            'short_description',
            'descriptions',
            'url',
            'github',
            'video',
        ]