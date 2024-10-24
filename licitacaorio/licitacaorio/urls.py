from django.contrib import admin
from django.urls import include, path

from licitacaorio.views import index

urlpatterns = [
    path("", index, name="home"),
    path("admin/", admin.site.urls, name="admin"),
    path("users/", include("users.urls"), name="users"),
    path("etp/", include("etp.urls"), name="etp"),
    path("tr/", include("tr.urls"), name="tr"),
]
