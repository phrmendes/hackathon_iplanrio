from django.urls import path

from etp import views

app_name = "etp"

urlpatterns = [
    path(
        "",
        views.adm_process_index,
        name="adm_process_index",
    ),
    path(
        "<int:adm_process_id>/",
        views.etp_index,
        name="etp_index",
    ),
    path(
        "<int:adm_process_id>/market_research/",
        views.market_research_index,
        name="market_research_index",
    ),
    path(
        "<int:adm_process_id>/market_research/create/",
        views.market_research_create,
        name="market_research_create",
    ),
    path(
        "<int:market_research_id>/market_research/delete/",
        views.market_research_delete,
        name="market_research_delete",
    ),
    path(
        "<int:adm_process_id>/contract_estimate/",
        views.contract_estimate_index,
        name="contract_estimate_index",
    ),
    path(
        "<int:adm_process_id>/contract_estimate/create/",
        views.contract_estimate_create,
        name="contract_estimate_create",
    ),
    path(
        "<int:contract_estimate_id>/contract_estimate/delete/",
        views.contract_estimate_delete,
        name="contract_estimate_delete",
    ),
    path(
        "<int:adm_process_id>/installment/",
        views.installment_index,
        name="installment_index",
    ),
    path(
        "<int:adm_process_id>/installment/fields/",
        views.installment_fields,
        name="installment_fields",
    ),
    path(
        "<int:adm_process_id>/summary/",
        views.summary_index,
        name="summary_index",
    ),
]
