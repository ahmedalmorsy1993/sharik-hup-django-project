from django.contrib import admin
from .models import Service,ServiceTranslation
from django.utils.html import format_html
from django import forms

# Register your models here.
class ServiceForm(forms.ModelForm):
    title_ar = forms.CharField()
    title_en = forms.CharField()
    content_ar = forms.CharField(widget=forms.Textarea)
    content_en = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Service
        fields = '__all__'



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("Icon", "is_active","title_ar","title_en")
    list_filter = ('is_active',)
    form = ServiceForm

    def Icon(self,obj) :
        return format_html('<img src={} width=100></img>',obj.icon.url)

    def title_ar(self,obj):
        return ServiceTranslation.objects.get(service_id=obj.id,locale='ar').title

    def title_en(self,obj):
        return ServiceTranslation.objects.get(service_id=obj.id,locale='en').title

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            ServiceTranslation.objects.bulk_create([
                ServiceTranslation(
                service_id = obj.id,
                locale='ar',
                title=form.cleaned_data['title_ar'],
                content=form.cleaned_data['content_ar']
                ),
                ServiceTranslation(
                service_id = obj.id,
                locale='en',
                title=form.cleaned_data['title_en'],
                content=form.cleaned_data['content_en']
                )
            ])
        else:
            ServiceTranslation.objects.filter(service_id = obj.id,locale='ar').update(
                title=form.cleaned_data['title_ar'],
                content=form.cleaned_data['content_ar']
            )
            ServiceTranslation.objects.filter(service_id = obj.id,locale='en').update(
                 title=form.cleaned_data['title_en'],
                content=form.cleaned_data['content_en']
            )

    class Meta :
        ordering = ('is_active',)
