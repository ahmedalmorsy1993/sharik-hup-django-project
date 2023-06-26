from django.db import models
from countries import models as countriesModels
from states import models as statesModels

# Create your models here.
class Center(models.Model):
    country=models.ForeignKey(countriesModels.Country,null=True,on_delete=models.SET_NULL)
    state=models.ForeignKey(statesModels.State,null=True,on_delete=models.SET_NULL)
    image=models.ImageField(upload_to='media/centers')


class CenterTranslation:
    locale=models.CharField(max_length=2)
    center=models.ForeignKey(Center,on_delete=models.CASCADE)
    title=models.CharField(max_length=255,unique=True)
