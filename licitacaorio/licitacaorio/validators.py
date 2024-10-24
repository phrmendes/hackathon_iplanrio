from django.core.exceptions import ValidationError

from licitacaorio.settings import ALLOWED_EMAIL_DOMAINS


def validate_email_domain(email: str) -> None:
    domain = email.split("@")[-1]

    if domain in ALLOWED_EMAIL_DOMAINS:
        return

    msg = f"Domínio inválido. Domínios permitidos: @{', @'.join(ALLOWED_EMAIL_DOMAINS)}"
    raise ValidationError(msg)


def validate_cnpj(cnpj: str) -> None:
    """Validate CNPJ number."""
    cnpj = "".join(filter(str.isdigit, cnpj))
    cnpj_length = 14

    if len(cnpj) != cnpj_length:
        msg = "CNPJ deve conter 14 dígitos."
        raise ValidationError(msg)

    if len(set(cnpj)) == 1:
        msg = "CNPJ inválido."
        raise ValidationError(msg)

    def calculate_digit(cnpj: str, weights: list[int]) -> int:
        limit = 2
        total = sum(int(digit) * weight for digit, weight in zip(cnpj, weights, strict=False))
        remainder = total % 11
        return 0 if remainder < limit else 11 - remainder

    weights_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    weights_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    check_digit_1 = calculate_digit(cnpj[:12], weights_1)
    check_digit_2 = calculate_digit(cnpj[:13], weights_2)

    if int(cnpj[12]) != check_digit_1 or int(cnpj[13]) != check_digit_2:
        msg = "CNPJ inválido."
        raise ValidationError(msg)
