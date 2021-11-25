from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import ToDo, Project
from user.models import User
from mixer.backend.django import mixer


class TestToDoViewSet(TestCase):
    def test_create_todo(self):
        project = mixer.blend(Project)
        user = mixer.blend(User)
        client = APIClient()
        data = {
            'project': project.name,
            'user': user.username,
            'title': 'test_title',
            'text': 'test_text',
            'is_active': True
        }
        response = client.post(
            f'/api/todos/',
            data,
            format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestProjectVeiwSet(APITestCase):
    def test_get_project(self):
        project = mixer.blend(Project)
        response = self.client.get(f'/api/projects/{project.id}/')
        for key in ('name', 'repository'):
            self.assertEqual(getattr(project, key), response.data[key])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
