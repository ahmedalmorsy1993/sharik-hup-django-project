from django.db import models

# Create your models here.
class Setting(models.Model):
    key = models.CharField(max_length=255,unique=True)
    value = models.JSONField()
    type = models.CharField(max_length=255)
