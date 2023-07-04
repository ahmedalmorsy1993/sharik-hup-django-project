from django.shortcuts import render
from .forms import StaticPageForm, StaticPageTransForm
from django.db import transaction
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils.translation import activate
@method_decorator([csrf_exempt,transaction.atomic], name='dispatch')
class CreateStaticPage(View):
    def post(self, request):
        # try:
            form = StaticPageForm(request.POST,request.FILES)
            if form.is_valid():
                static_page=form.save()
                for lang_code,lang_name in settings.LANGUAGES:
                 activate(lang_code)
                 translation_form = StaticPageTransForm(request.POST)
                 if translation_form.is_valid():
                     translation = translation_form.save(commit=False)
                     translation.static_page = static_page
                     translation.locale = lang_code
                     translation.save()
            return HttpResponse(form.cleaned_data)
                
        # except ValidationError as e:
        #     raise ValidationError(e)
        
    



@transaction.atomic
@csrf_exempt
def getStaticPage(request):
    pass
    # static_form = None
    # static_trans_form = None
    # saved_data = {}
    # if request.method == "POST":
    #     static_form = StaticPageForm(request.POST, request.FILES)
    #     if static_form.is_valid():
    #         saved_data = static_form.save()
    #         if "id" in saved_data:
    #             data = {
    #                 "title": request.POST.get("title"),
    #                 "content": request.POST.get("content"),
    #                 "static_page_id": saved_data.get("id"),
    #             }
    #         static_trans_form = StaticPageTransForm(data)
    #         if static_trans_form.is_valid():
    #             static_trans_form.save()
    # context = {"static_form": static_form, "static_trans_form": static_trans_form}
    # return render(request, "staticPages/index.html", context=context)
