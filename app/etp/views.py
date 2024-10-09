from django.http import HttpRequest, HttpResponse


def index(response: HttpRequest) -> HttpResponse:
    return HttpResponse(b"Hello, world. You're at the polls index.")
