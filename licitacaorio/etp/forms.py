import datetime
from typing import ClassVar

from django import forms

from etp import models
from licitacaorio.types import Inputs, Labels
from licitacaorio.validators import validate_cnpj


class AdmProcess(forms.ModelForm):
    """Form for creating an AdmProcess."""

    year = forms.IntegerField(
        min_value=2000,
        max_value=2100,
        widget=forms.NumberInput(attrs={"placeholder": "Ex: 2024"}),
        label="Ano de abertura",
    )

    class Meta:
        """Meta class for AdmProcess form."""

        model = models.AdmProcess
        fields = ("organization", "document_type", "year", "document_number")
        labels: ClassVar[Labels] = {
            "organization": "Secretaria ou orgão",
            "document_type": "Espécie documental",
            "document_number": "Número do documento",
        }
        widgets: ClassVar[Inputs] = {
            "organization": forms.TextInput(attrs={"placeholder": "Ex: SMS (Secretaria Municipal de Saúde)"}),
            "document_type": forms.TextInput(attrs={"placeholder": "Ex: PRO (Processo)"}),
            "document_number": forms.TextInput(attrs={"placeholder": "Ex: 12345"}),
        }


class ETP(forms.ModelForm):
    """Form for creating an ETP."""

    class Meta:
        """Meta class for ETP form."""

        model = models.ETP
        fields = ("justification", "requesting_area")
        labels: ClassVar[Labels] = {
            "justification": "Justificativa",
            "requesting_area": "Área solicitante",
        }


class MarketResearch(forms.ModelForm):
    """Form for creating a MarketResearch."""

    class Meta:
        """Meta class for MarketResearch form."""

        model = models.MarketResearch
        fields = ("product", "requester", "date", "source", "unit_price")
        labels: ClassVar[Labels] = {
            "product": "Produto",
            "requester": "Solicitante",
            "date": "Data",
            "source": "Fonte",
            "unit_price": "Preço unitário (R$)",
        }
        widgets: ClassVar[Inputs] = {
            "product": forms.TextInput(attrs={"placeholder": "Ex: Café"}),
            "requester": forms.TextInput(attrs={"placeholder": "Ex: XPTO LTDA"}),
            "source": forms.TextInput(attrs={"placeholder": "Ex: Portal de Compras"}),
            "date": forms.DateInput(attrs={"type": "date", "value": datetime.date.today}),
        }


class ContractEstimate(forms.ModelForm):
    """Form for creating a ContractEstimate."""

    cnpj = forms.CharField(
        max_length=18,
        validators=[validate_cnpj],
        widget=forms.TextInput(attrs={"placeholder": "Ex: 12.345.678/0001-90"}),
        label="CNPJ",
    )

    def clean_cnpj(self) -> str:
        """Clean and format CNPJ."""
        cnpj = self.cleaned_data["cnpj"]
        cnpj = "".join(filter(str.isdigit, cnpj))
        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"

    class Meta:
        """Meta class for ContractEstimate form."""

        model = models.ContractEstimate
        fields = ("cnpj", "supplier", "product", "description", "quantity", "unit_price")
        labels: ClassVar[Labels] = {
            "description": "Descrição",
            "product": "Produto",
            "quantity": "Quantidade",
            "supplier": "Fornecedor",
            "unit_price": "Preço unitário (R$)",
        }
        widgets: ClassVar[Inputs] = {
            "product": forms.TextInput(attrs={"placeholder": "Ex: Café"}),
            "description": forms.TextInput(attrs={"placeholder": "Ex: Moído e torrado, 500g"}),
            "quantity": forms.NumberInput(attrs={"placeholder": "Ex: 10", "min": 1}),
            "supplier": forms.TextInput(attrs={"placeholder": "Ex: XPTO LTDA"}),
        }


class Installment(forms.ModelForm):
    """Form for creating an Installment."""

    number = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(),
        label="Número de parcelas",
    )

    class Meta:
        """Meta class for Installment form."""

        model = models.Installment
        fields = (
            "justification",
            "due_date",
            "number",
            "value",
        )
        labels: ClassVar[Labels] = {
            "due_date": "Data de vencimento",
            "value": "Valor da parcela (R$)",
            "justification": "Justificativa",
        }
        widgets: ClassVar[Inputs] = {
            "due_date": forms.DateInput(attrs={"type": "date", "value": datetime.date.today}),
        }
