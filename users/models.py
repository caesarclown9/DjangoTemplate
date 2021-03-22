from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(verbose_name='ФИО', max_length=30, blank=True)

    def __str__(self):
        return self.username
