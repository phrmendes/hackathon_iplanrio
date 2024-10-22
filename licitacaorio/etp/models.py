from django.contrib.auth.models import User
from django.db import models
from djmoney.models.fields import MoneyField

from licitacaorio.settings import DEFAULT_CURRENCY


class AdmProcess(models.Model):
    """Model definition for AdmProcess."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="adm_processes")
    organization = models.CharField(max_length=3)
    document_type = models.CharField(max_length=3)
    year = models.IntegerField()
    document_number = models.CharField(max_length=5)

    def __str__(self) -> str:
        """Unicode representation of AdmProcess."""
        return f"AP(id={self.id}, process={self.organization}{self.document_type}{self.year}/{self.document_number})"


class ETP(models.Model):
    """Model definition for ETP."""

    adm_process = models.OneToOneField(AdmProcess, on_delete=models.CASCADE, related_name="etp")
    justification = models.TextField()
    requesting_area = models.CharField(max_length=100)

    def __str__(self) -> str:
        """Unicode representation of ETP."""
        return f"ETP(id={self.id}, adm_process={self.adm_process})"


class MarketResearch(models.Model):
    """Model definition for MarketResearch."""

    adm_process = models.ForeignKey(AdmProcess, on_delete=models.CASCADE, related_name="market_research")
    product = models.CharField(max_length=100)
    requester = models.CharField(max_length=100)
    date = models.DateField()
    source = models.CharField(max_length=100)
    unit_price = MoneyField(max_digits=10, decimal_places=2, default_currency=DEFAULT_CURRENCY)

    def __str__(self) -> str:
        """Unicode representation of MarketResearch."""
        return f"MR(id={self.id}, requester={self.requester},product={self.product}, price={self.unit_price})"


class ContractEstimate(models.Model):
    """Model definition for ContractEstimate."""

    adm_process = models.ForeignKey(AdmProcess, on_delete=models.CASCADE, related_name="contracts_estimates")
    cnpj = models.CharField(max_length=18)
    description = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)
    unit_price = MoneyField(max_digits=10, decimal_places=2, default_currency=DEFAULT_CURRENCY)

    def __str__(self) -> str:
        """Unicode representation of ContractEstimate."""
        return f"CE(id={self.id}, supplier={self.supplier}, product={self.product}, price={self.unit_price})"


class Installment(models.Model):
    """Model definition for Installment."""

    adm_process = models.OneToOneField(AdmProcess, on_delete=models.CASCADE, related_name="installments")
    due_date = models.DateField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    justification = models.TextField(blank=True)
    value = MoneyField(
        max_digits=10,
        decimal_places=2,
        default_currency=DEFAULT_CURRENCY,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        """Unicode representation of Installment."""
        return f"Installment(id={self.id}, value={self.value}, n={self.number})"
