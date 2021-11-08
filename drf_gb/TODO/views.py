from django.http import Http404
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from .filters import ProjectFilter
from .models import Project, ToDo
from .serializers import ProjectModelSerializer, ToDoModelSerializer


class ProjectPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectPagination
    filter_class = ProjectFilter


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoPagination
    filterset_fields = {
        'project': ['exact'],
        'created_at': ['gte', 'lte'],
    }

    def destroy(self, request, pk=None):
        try:
            todo = get_object_or_404(ToDo, pk=pk)
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        todo.is_active = False
        todo.save()
        return Response(status=status.HTTP_200_OK)
