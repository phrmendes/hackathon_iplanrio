from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from licitacaorio.settings import DASHBOARD_URL


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", {"dashboard": DASHBOARD_URL})
