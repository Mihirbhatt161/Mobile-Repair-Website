from django.db import models


# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=120)
    name=models.CharField(max_length=100)
    desc=models.TextField()