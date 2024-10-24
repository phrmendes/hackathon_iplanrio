from django.urls import path

from tr import views

app_name = "tr"

urlpatterns = [
    path(
        "",
        views.tr_index,
        name="index",
    ),
    path(
        "list/",
        views.tr_list,
        name="list",
    ),
    path(
        "<int:tr_id>/delete/",
        views.tr_delete,
        name="delete",
    ),
    path(
        "<int:tr_id>/risk_matrix/",
        views.risk_matrix_index,
        name="risk_matrix_index",
    ),
    path(
        "<int:tr_id>/risk_matrix/create/",
        views.risk_matrix_create,
        name="risk_matrix_create",
    ),
    path(
        "risk_matrix/delete/<int:risk_matrix_id>/",
        views.risk_matrix_delete,
        name="risk_matrix_delete",
    ),
    path(
        "<int:tr_id>/summary/",
        views.summary_index,
        name="summary_index",
    ),
]
