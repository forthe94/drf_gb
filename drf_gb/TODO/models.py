from django.db import models
from user.models import User
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=50)
    repository = models.URLField(unique=True)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    project = models.ForeignKey(Project, related_name='todos', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
