from django.db import models
from django.utils.text import slugify


class StaticPage(models.Model):
    image = models.ImageField(upload_to="images/media")
    is_active = models.BooleanField(default=True)


class StaticPageTrans(models.Model):
    locale = models.CharField(max_length=50)
    static_page = models.ForeignKey(
        StaticPage, related_name="static_page_trans", on_delete=models.CASCADE
    )
    slug = models.SlugField(unique=True)
    page_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    sub_title = models.CharField(null=True, blank=True, max_length=255)
    btn_title = models.CharField(null=True, blank=True, max_length=255)
    btn_link = models.CharField(null=True, blank=True, max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(StaticPageTrans, self).save(*args, **kwargs)
