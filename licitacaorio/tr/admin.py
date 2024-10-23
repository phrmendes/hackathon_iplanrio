from django.contrib import admin

from tr import models

models = [
    models.TR,
    models.RiskMatrix,
]

for model in models:
    admin.site.register(model)
