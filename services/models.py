from django.db import models

# Create your models here.

class Service(models.Model):
    icon = models.ImageField(upload_to ='media/services')
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "services"

class ServiceTranslation(models.Model):
    locale = models.CharField(max_length=2)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True)

    class Meta:
        db_table = "service_translations"
