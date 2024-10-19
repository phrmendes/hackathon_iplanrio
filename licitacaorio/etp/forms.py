from typing import ClassVar

from django import forms

from etp import models


class ETPForm(forms.ModelForm):
    """Form for creating an ETP."""

    class Meta:
        """Meta class for ETPForm."""

        model = models.ETP
        fields = ("adm_process", "justification", "requesting_area")
        labels: ClassVar[dict[str, str]] = {
            "adm_process": "Processo administrativo",
            "justification": "Justificativa",
            "requesting_area": "Área solicitante",
        }


class MarketResearchForm(forms.ModelForm):
    """Form for creating a MarketResearch."""

    class Meta:
        """Meta class for MarketResearchForm."""

        model = models.MarketResearch
        fields = ("product", "requester", "date", "source", "unit_price")
        labels: ClassVar[dict[str, str]] = {
            "product": "Produto",
            "requester": "Solicitante",
            "date": "Data",
            "source": "Fonte",
            "unit_price": "Preço unitário",
        }


class ContractEstimateForm(forms.ModelForm):
    """Form for creating a ContractEstimate."""

    class Meta:
        """Meta class for ContractEstimateForm."""

        model = models.ContractEstimate
        fields = ("cnpj", "description", "product", "quantity", "supplier", "unit_price")
        labels: ClassVar[dict[str, str]] = {
            "cnpj": "CNPJ",
            "description": "Descrição",
            "product": "Produto",
            "quantity": "Quantidade",
            "supplier": "Fornecedor",
            "unit_price": "Preço unitário",
        }


class InstallmentForm(forms.ModelForm):
    """Form for creating an Installment."""

    class Meta:
        """Meta class for Install Form."""

        model = models.Installment
        fields = ("due_date", "installment", "installment_number", "installment_value", "justification", "value")
        labels: ClassVar[dict[str, str]] = {
            "due_date": "Data de vencimento",
            "installment": "Parcela",
            "installment_number": "Número da parcela",
            "installment_value": "Valor da parcela",
            "justification": "Justificativa",
            "value": "Valor",
        }
