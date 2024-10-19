from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import ETPForm


@login_required
@require_http_methods(["GET", "POST"])
def etp(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ETPForm(request.POST)

        if form.is_valid():
            # form.save()
            return render(request, "etp/ok.html", {"form": form, "htmx": True})
    else:
        form = ETPForm()

    return render(request, "etp/etp.html", {"form": form, "htmx": True})
