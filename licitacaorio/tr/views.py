from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET, require_http_methods

from tr import forms, models


@login_required
@require_http_methods(["GET", "POST"])
def tr_index(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.TR(request.POST)

        if form.is_valid():
            tr = form.save(commit=False)
            tr.save()

            return redirect("tr:risk_matrix_index", tr_id=tr.pk)

        return render(request, "tr/tr/index.html", {"form": form})

    return render(request, "tr/tr/index.html", {"form": forms.TR()})


@login_required
@require_GET
def tr_list(request: HttpRequest) -> HttpResponse:
    tr_list = models.TR.objects.all().order_by("-id")
    paginator = Paginator(tr_list, 5)
    page = request.GET.get("page", 1)
    trs = paginator.get_page(page)

    return render(request, "tr/list.html", {"trs": trs})


@login_required
@require_http_methods(["DELETE"])
def tr_delete(request: HttpRequest, tr_id: int) -> HttpResponse:
    try:
        tr = get_object_or_404(models.TR, pk=tr_id)
        tr.delete()

        return render(request, "empty.html")
    except models.TR.DoesNotExist:
        return HttpResponse(status=404)


@login_required
@require_GET
def risk_matrix_index(request: HttpRequest, tr_id: int) -> HttpResponse:
    tr = get_object_or_404(models.TR, pk=tr_id)
    risk_matrix = models.RiskMatrix.objects.filter(tr=tr)

    context = {
        "form": forms.RiskMatrix(),
        "risk_matrix": risk_matrix,
        "tr_id": tr_id,
    }

    return render(request, "tr/risk_matrix/index.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def risk_matrix_create(request: HttpRequest, tr_id: int) -> HttpResponse:
    if request.method == "POST":
        form = forms.RiskMatrix(request.POST)

        if form.is_valid():
            tr = get_object_or_404(models.TR, pk=tr_id)

            risk_matrix = form.save(commit=False)
            risk_matrix.tr = tr
            risk_matrix.save()

            context = {"row": risk_matrix}

            return render(request, "tr/risk_matrix/partials/list.html", context)

        context = {"form": form, "tr_id": tr_id}

        return render(request, "tr/risk_matrix/partials/form.html", context)

    context = {"form": forms.RiskMatrix()}

    return render(request, "tr/risk_matrix/partials/form.html", context)


@login_required
@require_http_methods(["DELETE"])
def risk_matrix_delete(request: HttpRequest, risk_matrix_id: int) -> HttpResponse:
    try:
        risk_matrix_row = get_object_or_404(models.RiskMatrix, pk=risk_matrix_id)
        risk_matrix_row.delete()

        return render(request, "empty.html")
    except models.RiskMatrix.DoesNotExist:
        return HttpResponse(status=404)


@login_required
@require_GET
def summary_index(request: HttpRequest, tr_id: int) -> HttpResponse:
    tr = get_object_or_404(models.TR, pk=tr_id)
    risk_matrix = models.RiskMatrix.objects.filter(tr=tr)

    context = {
        "risk_matrix": risk_matrix,
        "tr": tr,
    }

    return render(request, "tr/summary/index.html", context)
