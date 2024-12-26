from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=20)
    active_code = models.CharField(max_length=10)
    token = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

