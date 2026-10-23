# journaux/models.py
from django.db import models


class JournalChantier(models.Model):
    METEO_CHOICES = [
        ("soleil", "Ensoleillé"),
        ("nuage", "Nuageux"),
        ("pluie", "Pluvieux"),
        ("vent", "Venteux"),
    ]

    chantier = models.CharField(max_length=150)
    date = models.DateField()
    meteo = models.CharField(max_length=20, choices=METEO_CHOICES)
    effectif = models.PositiveIntegerField(default=0)
    travaux_realises = models.TextField()
    observations = models.TextField(blank=True)
    incidents = models.TextField(blank=True)
    cree_le = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-cree_le"]
        verbose_name_plural = "Journaux de chantier"

    def __str__(self):
        return f"{self.chantier} - {self.date}"


class PhotoJournal(models.Model):
    journal = models.ForeignKey(
        JournalChantier,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    image = models.ImageField(upload_to="journaux/%Y/%m/")
    legende = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Photo - {self.journal}"
