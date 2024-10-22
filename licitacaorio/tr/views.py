from django.http import HttpRequest, HttpResponse


def index(response: HttpRequest) -> HttpResponse:
    return HttpResponse(b"TR app")
