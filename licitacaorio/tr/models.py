from django.db import models

from etp.models import AdmProcess


class TR(models.Model):
    """Model definition for TR."""

    adm_process = models.OneToOneField(AdmProcess, on_delete=models.CASCADE, related_name="tr")
    objective = models.TextField()
    justification = models.TextField()
    description = models.TextField()
    service_location = models.CharField(max_length=100)
    scheduled_date = models.DateField()

    def __str__(self) -> str:
        """Unicode representation of TR."""
        return f"TR(id={self.id}, adm_process={self.adm_process})"


class RiskMatrix(models.Model):
    """Model definition for RiskMatrix."""

    tr = models.ForeignKey(TR, on_delete=models.CASCADE, related_name="risk_matrix")
    type = models.CharField(max_length=100)
    risk = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100, blank=True)
    probability = models.PositiveIntegerField()
    impact = models.PositiveIntegerField()
    strategy = models.CharField(max_length=100)
    mitigation = models.CharField(max_length=100)
    in_charge = models.CharField(max_length=100)

    def __str__(self) -> str:
        """Unicode representation of RiskMatrix."""
        return f"RM(id={self.id}, tr={self.tr})"

    @property
    def probability_times_impact(self) -> int:
        """Calculate the probability times impact."""
        return self.probability * self.impact
