from django.urls import path

from . import views

app_name = "etp"

urlpatterns = [
    path("", views.etp, name="etp"),
]
