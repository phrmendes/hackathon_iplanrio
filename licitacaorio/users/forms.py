from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreation(UserCreationForm):
    """Form for creating an user."""

    class Meta:
        """Meta class for ETPForm."""

        model = User
        fields = ("first_name", "last_name", "username", "email")
