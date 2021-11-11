from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, ToDo
from rest_framework import serializers


class ProjectModelSerializer(HyperlinkedModelSerializer):
    users = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(HyperlinkedModelSerializer):
    project = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = ToDo
        fields = '__all__'
