from typing import Any, Dict
from django import forms
from .models import StaticPageTrans, StaticPage


class StaticPageTransForm(forms.ModelForm):
    class Meta:
        model = StaticPageTrans
        fields = [
            "title",
            "content",
            "sub_title",
            "btn_title",
            "btn_link",
        ]


class StaticPageForm(forms.ModelForm):
    class Meta:
        model = StaticPage
        fields = ["image"]
