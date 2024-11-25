from django.db import models
from django.contrib.auth.models import AbstractUser


class signup_model(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    email=models.EmailField()


class Login_model(AbstractUser):
    username=models.CharField(max_length=200, unique=True)
    password=models.CharField(max_length=200)
    email=models.EmailField()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"