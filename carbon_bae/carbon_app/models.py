from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    bio = models.TextField(blank=True)
    image_url = models.URLField(max_length=100)

class PostImage(models.Model):
    datetime = models.DateTimeField(auto_now=True,blank=False,null=False)
    image_url = models.URLField(max_length=100)
