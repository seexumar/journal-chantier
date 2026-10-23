# journaux/admin.py
from django.contrib import admin
from .models import JournalChantier, PhotoJournal


class PhotoJournalInline(admin.TabularInline):
    model = PhotoJournal
    extra = 1


@admin.register(JournalChantier)
class JournalChantierAdmin(admin.ModelAdmin):
    list_display = ("chantier", "date", "meteo", "effectif")
    list_filter = ("meteo", "date")
    search_fields = ("chantier", "travaux_realises")
    inlines = [PhotoJournalInline]
