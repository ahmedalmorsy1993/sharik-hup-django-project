from django.shortcuts import render
from .forms import StaticPageForm, StaticPageTransForm
from django.db import transaction


def createStaticPage(request):
    if request.method == "POST":
        print(request, "request")


@transaction.atomic
def getStaticPage(request):
    static_form = None
    static_trans_form = None
    saved_data = {}
    if request.method == "POST":
        static_form = StaticPageForm(request.POST, request.FILES)
        if static_form.is_valid():
            saved_data = static_form.save()
            if "id" in saved_data:
                data = {
                    "title": request.POST.get("title"),
                    "content": request.POST.get("content"),
                    "static_page_id": saved_data.get("id"),
                }
            static_trans_form = StaticPageTransForm(data)
            if static_trans_form.is_valid():
                static_trans_form.save()
    context = {"static_form": static_form, "static_trans_form": static_trans_form}
    return render(request, "staticPages/index.html", context=context)
