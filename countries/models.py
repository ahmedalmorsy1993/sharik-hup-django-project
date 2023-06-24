from django.db import models

# Create your models here.
class Country(models.Model):
    is_active = models.BooleanField(default=True)

class CountryTranslation(models.Model):
    locale = models.CharField(max_length=2)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,unique=True)
