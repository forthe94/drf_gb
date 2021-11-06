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
        article = get_object_or_404(ToDo, pk=pk)
        if not article:
            return Response(status=status.HTTP_404_NOT_FOUND)
        article.is_active = False
        article.save()
        return Response(status=status.HTTP_200_OK)
