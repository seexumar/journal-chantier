# journaux/views.py
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import JournalChantierForm
from .models import JournalChantier, PhotoJournal


def journal_list(request):
    journaux = JournalChantier.objects.prefetch_related("photos")

    recherche = request.GET.get("recherche", "").strip()
    meteo = request.GET.get("meteo", "").strip()

    if recherche:
        journaux = journaux.filter(
            Q(chantier__icontains=recherche)
            | Q(travaux_realises__icontains=recherche)
            | Q(observations__icontains=recherche)
        )

    if meteo:
        journaux = journaux.filter(meteo=meteo)

    if request.method == "POST":
        form = JournalChantierForm(request.POST, request.FILES)

        if form.is_valid():
            journal = form.save()

            for photo in form.cleaned_data["photos"]:
                PhotoJournal.objects.create(
                    journal=journal,
                    image=photo,
                )

            messages.success(request, "Le journal a bien été enregistré.")
            return redirect("journal-list")
    else:
        form = JournalChantierForm()

    return render(
        request,
        "journaux/journal_list.html",
        {
            "form": form,
            "journaux": journaux,
            "recherche": recherche,
            "meteo": meteo,
        },
    )


def journal_detail(request, pk):
    journal = get_object_or_404(
        JournalChantier.objects.prefetch_related("photos"),
        pk=pk,
    )
    return render(
        request,
        "journaux/journal_detail.html",
        {"journal": journal},
    )
