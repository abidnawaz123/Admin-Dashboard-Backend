from django.db import models

class LatestCustomers(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
