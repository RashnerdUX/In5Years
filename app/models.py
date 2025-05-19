from django.db import models


# Create your models here.
class TimeCapsule(models.Model):
    title = models.CharField(max_length=30)
    message = models.CharField(max_length=5000)
