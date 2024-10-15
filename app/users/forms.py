from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form."""

    class Meta(UserCreationForm.Meta):
        """Meta class."""

        fields = (
            *UserCreationForm.Meta.fields,
            "email",
            "first_name",
            "last_name",
        )

    field_order = ("first_name", "last_name", "username", "email", "password1", "password2")
    first_name = forms.CharField(label="Primeiro nome", max_length=30, required=True)
    last_name = forms.CharField(label="Último nome", max_length=30, required=True)
