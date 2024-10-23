import datetime
from typing import ClassVar

from django import forms

from etp.models import AdmProcess
from licitacaorio.types import Inputs, Labels
from tr import models


class TR(forms.ModelForm):
    """Form for creating an TR."""

    adm_process = forms.ModelChoiceField(
        queryset=AdmProcess.objects.all(),
        label="Processo Administrativo (ETP)",
        empty_label="Selecione um ETP",
    )

    class Meta:
        """Meta class for TR form."""

        model = models.TR
        fields = ("adm_process", "objective", "justification", "description", "service_location", "scheduled_date")
        labels: ClassVar[Labels] = {
            "adm_process": "Processo Administrativo",
            "objective": "Objetivo",
            "justification": "Justificativa",
            "description": "Descrição",
            "service_location": "Local de prestação do serviço",
            "scheduled_date": "Data agendada",
        }
        widgets: ClassVar[Inputs] = {
            "scheduled_date": forms.DateInput(attrs={"type": "date", "value": datetime.date.today}),
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

        widgets: ClassVar[Inputs] = {
            "probability": forms.NumberInput(attrs={"type": "number", "min": 1, "max": 100}),
            "impact": forms.NumberInput(attrs={"type": "number", "min": 1, "max": 100}),
        }
