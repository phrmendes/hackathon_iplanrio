from typing import TYPE_CHECKING

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import now
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from etp import forms, models
from licitacaorio.utils import StatusChoices

if TYPE_CHECKING:
    from licitacaorio.types import Context


@login_required
@require_http_methods(["GET", "POST"])
def adm_process_index(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.AdmProcess(request.POST)

        if form.is_valid():
            adm_process = form.save(commit=False)
            adm_process.user = request.user
            adm_process.save()

            return redirect("etp:etp_index", adm_process_id=adm_process.pk)

        return render(request, "etp/adm_process/index.html", {"form": form})

    return render(request, "etp/adm_process/index.html", {"form": forms.AdmProcess()})


@login_required
@require_GET
def adm_process_list(request: HttpRequest) -> HttpResponse:
    adm_process_list = models.AdmProcess.objects.filter(user=request.user).order_by("-id")
    paginator = Paginator(adm_process_list, 5)
    page = request.GET.get("page", 1)
    adm_processes = paginator.get_page(page)

    return render(request, "etp/partials/list.html", {"adm_processes": adm_processes})


@login_required
@require_http_methods(["DELETE"])
def adm_process_delete(request: HttpRequest, adm_process_id: int) -> HttpResponse:
    adm_process = get_object_or_404(models.AdmProcess, pk=adm_process_id)
    adm_process.delete()

    return render(request, "empty.html")


@login_required
@require_http_methods(["GET", "POST"])
def etp_index(request: HttpRequest, adm_process_id: int) -> HttpResponse:
    context: Context = {"adm_process_id": adm_process_id}

    if request.method == "POST":
        form = forms.ETP(request.POST)
        if form.is_valid():
            etp = form.save(commit=False)
            etp.adm_process = get_object_or_404(models.AdmProcess, pk=adm_process_id)
            etp.save()

            return redirect("etp:market_research_index", adm_process_id=adm_process_id)

        context["form"] = form

        return render(request, "etp/etp/index.html", context)

    context["form"] = forms.ETP()

    return render(request, "etp/etp/index.html", context)


@login_required
@require_POST
def etp_change_status(request: HttpRequest, adm_process_id: int) -> HttpResponse:
    adm_process = get_object_or_404(models.AdmProcess, id=adm_process_id)
    etp = models.ETP.objects.filter(adm_process=adm_process).first()

    if etp.status == "Pendente":
        status = StatusChoices.FINISHED.value
        previous_status = StatusChoices.PENDING.value
        concluded_at = now()
    else:
        status = StatusChoices.PENDING.value
        previous_status = StatusChoices.FINISHED.value
        concluded_at = None

    etp.status = status
    etp.concluded_at = concluded_at
    etp.previous_status = previous_status
    etp.save()

    return render(request, "etp/partials/list_item.html", {"adm_process": adm_process})


@login_required
@require_GET
def market_research_index(request: HttpRequest, adm_process_id: int) -> HttpResponse:
    adm_process = get_object_or_404(models.AdmProcess, pk=adm_process_id)
    market_researches = models.MarketResearch.objects.filter(adm_process=adm_process)

    context = {
        "form": forms.MarketResearch(),
        "market_researches": market_researches,
        "adm_process_id": adm_process_id,
    }

    return render(request, "etp/market_research/index.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def market_research_create(request: HttpRequest, adm_process_id: int) -> HttpResponse:
    if request.method == "POST":
        form = forms.MarketResearch(request.POST)

        if form.is_valid():
            adm_process = get_object_or_404(models.AdmProcess, pk=adm_process_id)

            market_research = form.save(commit=False)
            market_research.adm_process = adm_process
            market_research.save()

            context = {"market_research": market_research}

            return render(request, "etp/market_research/partials/list.html", context)

        context = {"form": form, "adm_process_id": adm_process_id}

        return render(request, "etp/contract_estimate/partials/form.html", context)

    context = {"form": forms.MarketResearch()}

    return render(request, "etp/market_research/partials/form.html", context)


@login_required
@require_http_methods(["DELETE"])
def market_research_delete(request: HttpRequest, market_research_id: int) -> HttpResponse:
    try:
        market_research = get_object_or_404(models.MarketResearch, pk=market_research_id)
        market_research.delete()

        return render(request, "empty.html")
    except models.MarketResearch.DoesNotExist:
        return HttpResponse(status=404)


@login_required
@require_GET
def contract_estimate_index(request: HttpRequest, adm_process_id: int) -> HttpResponse:
    adm_process = get_object_or_404(models.AdmProcess, pk=adm_process_id)
    contract_estimates = models.ContractEstimate.objects.filter(adm_process=adm_process)

    context = {
        "form": forms.ContractEstimate(),
        "contract_estimates": contract_estimates,
        "adm_process_id": adm_process_id,
    }

    return render(request, "etp/contract_estimate/index.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def contract_estimate_create(request: HttpRequest, adm_process_id: int) -> HttpResponse:
    if request.method == "POST":
        form = forms.ContractEstimate(request.POST)

        if form.is_valid():
            adm_process = get_object_or_404(models.AdmProcess, pk=adm_process_id)

            contract_estimate = form.save(commit=False)
            contract_estimate.adm_process = adm_process
            contract_estimate.save()

            context = {"contract_estimate": contract_estimate}

            return render(request, "etp/contract_estimate/partials/list.html", context)

        context = {"form": form, "adm_process_id": adm_process_id}

        return render(request, "etp/contract_estimate/partials/form.html", context)

    context = {"form": forms.ContractEstimate()}

    return render(request, "etp/contract_estimate/partials/form.html", context)


@login_required
@require_http_methods(["DELETE"])
def contract_estimate_delete(request: HttpRequest, contract_estimate_id: int) -> HttpResponse:
    try:
        contract_estimate = get_object_or_404(models.ContractEstimate, pk=contract_estimate_id)
        contract_estimate.delete()

        return render(request, "empty.html")
    except models.ContractEstimate.DoesNotExist:
        return HttpResponse(status=404)


@login_required
@require_GET
def installment_index(request: HttpRequest, adm_process_id: int) -> HttpResponse:
    context = {"form": forms.Installment(), "adm_process_id": adm_process_id}

    return render(request, "etp/installment/index.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def installment_fields(request: HttpRequest, adm_process_id: int) -> HttpResponse:
    context: Context = {"adm_process_id": adm_process_id}

    if request.method == "GET":
        context["enable_installment"] = request.GET.get("enable_installment") == "on"
        form = forms.Installment()
    else:
        form = forms.Installment(request.POST)
        if form.is_valid():
            adm_process = get_object_or_404(models.AdmProcess, pk=adm_process_id)
            installment = form.save(commit=False)
            installment.adm_process = adm_process
            installment.save()

            return render(request, "etp/installment/partials/success.html", context)

    context["form"] = form

    return render(request, "etp/installment/partials/fields.html", context)


@login_required
@require_GET
def summary_index(request: HttpRequest, adm_process_id: int) -> HttpResponse:
    adm_process = get_object_or_404(models.AdmProcess, pk=adm_process_id)
    etp = models.ETP.objects.filter(adm_process=adm_process).first()
    market_researches = models.MarketResearch.objects.filter(adm_process=adm_process)
    contracts_estimates = models.ContractEstimate.objects.filter(adm_process=adm_process)
    installment = models.Installment.objects.filter(adm_process=adm_process).first()

    context = {
        "adm_process_id": adm_process_id,
        "etp": etp,
        "adm_process": adm_process,
        "market_researches": market_researches,
        "contracts_estimates": contracts_estimates,
        "installment": installment,
    }

    return render(request, "etp/summary/index.html", context)
