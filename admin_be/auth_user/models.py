from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    cv = models.FileField(upload_to="csv/",null=True,blank=True)
