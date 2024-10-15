from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from users.utils import validate_email_domain

from .forms import CustomUserCreationForm


@require_http_methods(["GET", "POST"])
def create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            try:
                validate_email_domain(form.cleaned_data["email"])
            except ValidationError as error:
                form.add_error("email", error)
                return render(request, "users/create.html", {"form": form})

            auth.login(request, form.save())
            return redirect("home")
    else:
        form = CustomUserCreationForm()

    return render(request, "users/create.html", {"form": form})


@require_http_methods(["GET", "POST"])
def login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})


@login_required
@require_http_methods(["GET", "POST"])
def logout(request: HttpRequest) -> HttpResponse:
    auth.logout(request)
    return redirect("home")


@login_required
@require_http_methods(["GET", "POST"])
def update(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            auth.update_session_auth_hash(request, form.user)
            return redirect("users/success.html")

    else:
        form = PasswordChangeForm(request.user)

    return render(request, "users/update.html", {"form": form})
