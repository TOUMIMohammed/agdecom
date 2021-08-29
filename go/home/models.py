from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class globalConfig(models.Model):
    name = models.CharField(max_length=200,default="Tropical Deliveries")
    year = models.CharField(max_length=200,default="2021")
    title = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.title