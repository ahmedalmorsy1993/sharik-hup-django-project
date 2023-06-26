from django.db import models
from countries import models as countryModels

# Create your models here.
class State(models.Model):
    is_active = models.BooleanField(default=True)
    country = models.ForeignKey(countryModels.Country,null=True,on_delete=models.SET_NULL)

class StateTranslation(models.Model):
    locale=models.CharField(max_length=2)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,unique=True)
