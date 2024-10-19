from django.contrib.auth.models import User
from django.db import models


class ETP(models.Model):
    """Model definition for ETP."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adm_process = models.CharField(max_length=100)
    justification = models.TextField()
    requesting_area = models.CharField(max_length=100)

    def __str__(self) -> str:
        """Unicode representation of ETP."""
        return f"ETP(id={self.id}, adm_process={self.adm_process})"


class MarketResearch(models.Model):
    """Model definition for MarketResearch."""

    etp = models.ForeignKey(ETP, on_delete=models.CASCADE, related_name="market_research")
    product = models.CharField(max_length=100)
    requester = models.CharField(max_length=100)
    date = models.DateField()
    source = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        """Unicode representation of MarketResearch."""
        return f"MR(id={self.id}, requester={self.requester},product={self.product}, price={self.unit_price})"


class ContractEstimate(models.Model):
    """Model definition for ContractEstimate."""

    etp = models.ForeignKey(ETP, on_delete=models.CASCADE, related_name="contracts_estimates")
    cnpj = models.CharField(max_length=14)
    description = models.TextField()
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        """Unicode representation of ContractEstimate."""
        return f"CE(id={self.id}, supplier={self.supplier}, product={self.product}, price={self.unit_price})"


class Installment(models.Model):
    """Model definition for Installment."""

    etp = models.OneToOneField(ETP, on_delete=models.CASCADE, related_name="installments")
    due_date = models.DateField()
    installment = models.BooleanField()
    installment_number = models.IntegerField()
    installment_value = models.IntegerField()
    justification = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        """Unicode representation of Installment."""
        return f"Installment(id={self.id}, value={self.value}, n={self.installment_number})"
