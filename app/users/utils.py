from django.core.exceptions import ValidationError

from licitacaorio.settings import ALLOWED_EMAIL_DOMAINS


def validate_email_domain(email: str) -> None:
    domain = email.split("@")[-1]

    if domain in ALLOWED_EMAIL_DOMAINS:
        return

    msg = f"Domínio inválido. Domínios permitidos: @{', @'.join(ALLOWED_EMAIL_DOMAINS)}"
    raise ValidationError(msg)
