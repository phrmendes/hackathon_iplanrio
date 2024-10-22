from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from licitacaorio.validators import validate_email_domain


class UserCreation(UserCreationForm):
    """Form for creating an user."""

    email = forms.EmailField(
        validators=[validate_email_domain],
        widget=forms.TextInput(attrs={"placeholder": "Ex: fulano@prefeitura.rio"}),
        label="E-mail",
    )

    class Meta:
        """Meta class for ETPForm."""

        model = User
        fields = ("first_name", "last_name", "username", "email")
