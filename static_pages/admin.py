from django.contrib import admin
from .models import StaticPage, StaticPageTrans


class StaticPageTransAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


admin.site.register(StaticPageTrans, StaticPageTransAdmin)
admin.site.register(StaticPage)

# Register your models here.
