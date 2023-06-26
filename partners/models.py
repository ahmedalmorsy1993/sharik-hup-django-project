from django.db import models

# Create your models here.
class Partner(models.Model):
    image = models.ImageField(upload_to ='media/partners')
    is_active = models.BooleanField(default=True)
    alt_image = models.CharField(max_length=255)
