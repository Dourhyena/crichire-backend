from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CHOICES = (
        ('player', 'Player'),
        ('manager', 'Manager')
    )
    role = models.CharField(max_length=7, choices=CHOICES)


