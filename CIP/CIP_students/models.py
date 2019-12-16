from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    avatar = models.FileField(upload_to='media/avatars',default='../static/img/logo.svg',null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)
    status = models.CharField(max_length=30,null=False,default='student')
class Note(models.Model):
    text = models.TextField(default='...',null=False)
    date = models.DateTimeField(null = False)
    author = models.ForeignKey(CustomUser, on_delete = models.SET_NULL,null = True)
    whom = models.CharField(max_length = 100,null = True)

    def __str__(self):
        return self.text
