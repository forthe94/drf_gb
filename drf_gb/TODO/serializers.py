from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, ToDo
from rest_framework import serializers

from user.models import User


class ProjectModelSerializer(HyperlinkedModelSerializer):
    users = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(HyperlinkedModelSerializer):
    project = serializers.SlugRelatedField(queryset=Project.objects.all(), slug_field='name')
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = ToDo
        fields = '__all__'
