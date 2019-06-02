from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    picture = models.CharField(max_length=500, null=True, blank=True)
