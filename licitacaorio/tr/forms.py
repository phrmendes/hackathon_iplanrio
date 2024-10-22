from typing import ClassVar

from django import forms

from etp import models
from licitacaorio.types import Labels


class TR(forms.ModelForm):
    """Form for creating an TR."""

    class Meta:
        """Meta class for TR form."""

        model = models.TR
        fields = ("objective", "justification", "description", "service_location", "scheduled_date")
        labels: ClassVar[Labels] = {
            "objective": "Objetivo",
            "justification": "Justificativa",
            "description": "Descrição",
            "service_location": "Local de prestação do serviço",
            "scheduled_date": "Data agendada",
        }


class RiskMatrix(forms.ModelForm):
    """Form for creating a RiskMatrix."""

    class Meta:
        """Meta class for RiskMatrix form."""

        model = models.RiskMatrix
        fields = (
            "type",
            "risk",
            "category",
            "subcategory",
            "probability",
            "impact",
            "strategy",
            "mitigation",
            "in_charge",
        )
        labels: ClassVar[Labels] = {
            "type": "Tipo",
            "risk": "Risco",
            "category": "Categoria",
            "subcategory": "Subcategoria",
            "probability": "Probabilidade",
            "impact": "Impacto",
            "strategy": "Estratégia",
            "mitigation": "Mitigação",
            "in_charge": "Responsável",
        }
