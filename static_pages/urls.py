from django.urls import path
from .views import CreateStaticPage, getStaticPage

urlpatterns = [
    path("", view=getStaticPage, name="static_page"),
    path("static-pages/", view=CreateStaticPage.as_view(), name="create_static_page"),
]
