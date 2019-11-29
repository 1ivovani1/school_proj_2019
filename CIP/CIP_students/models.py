from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    avatar = models.FileField(upload_to='media/avatars',default='static/img/logo.png',null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)

# Create your models here.
