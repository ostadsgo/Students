from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=2500)


class GroupPremission(models.Model):
    group_id = models.IntegerField()
    premission_id = models.IntegerField()
