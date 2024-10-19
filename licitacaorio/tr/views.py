from django.http import HttpRequest, HttpResponse


def tr(response: HttpRequest) -> HttpResponse:
    return HttpResponse(b"TR app")
