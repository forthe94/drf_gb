from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


from django.db import models


class User(AbstractUser):
    groups = None
    user_permissions = None
    pass
