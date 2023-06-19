from django.urls import path
from .views import createStaticPage, getStaticPage

urlpatterns = [
    path("", view=getStaticPage, name="static_page"),
    path("static-pages/", view=createStaticPage, name="create_static_page"),
]
