from django import forms
from .models import StaticPageTrans, StaticPage


class StaticPageTransForm(forms.ModelForm):
    class Meta:
        model = StaticPageTrans
        fields = "__all__"

class StaticPageForm(forms.ModelForm):
    class Meta:
        model = StaticPage
        fields = ["image"]
