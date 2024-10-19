from django.contrib import admin

from etp import models

models = [
    models.ETP,
    models.MarketResearch,
    models.ContractEstimate,
    models.Installment,
]

for model in models:
    admin.site.register(model)
