from django.urls import path

from . import views

app_name = "tr"

urlpatterns = [
    path("", views.tr, name="tr"),
]
