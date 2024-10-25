from enum import Enum


class StatusChoices(Enum):
    """StatusChoices definition."""

    PENDING = "Pendente"
    FINISHED = "Concluído"

    @classmethod
    def choices(cls) -> list[tuple[str, str]]:
        """Return a list of tuples with the choices."""
        return [(choice.value, choice.value) for choice in cls]
