from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
class User(AbstractUser):
    name=models.CharField(max_length=100, blank=True, null=True)
    email=models.EmailField(max_length=200,unique=True)
    phone =models.CharField(max_length=10, blank=True, null=True)
    user_type=models.CharField(max_length=10,
                               choices=
                               [
                                   ("admin","admin"),
                                   ("teacher","teacher"),
                                   ("student","student"),
                               ],
                               default='admin')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


import os

def create_path(instance, filename):
    return os.path.join(
        instance.user.user_type,
        instance.user.username,
        filename
    )

class Gallery(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=create_path,null=True)
    datetime=models.DateTimeField(auto_now=True)
