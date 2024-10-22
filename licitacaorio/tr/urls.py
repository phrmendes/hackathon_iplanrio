from django.urls import path

from tr import views

app_name = "tr"

urlpatterns = [
    path("", views.index, name="index"),
]
