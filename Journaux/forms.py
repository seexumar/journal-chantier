# journaux/forms.py
from django import forms
from .models import JournalChantier


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_clean = super().clean

        if isinstance(data, (list, tuple)):
            return [single_clean(item, initial) for item in data]

        return [single_clean(data, initial)] if data else []


class JournalChantierForm(forms.ModelForm):
    photos = MultipleFileField(required=False)

    class Meta:
        model = JournalChantier
        fields = [
            "chantier",
            "date",
            "meteo",
            "effectif",
            "travaux_realises",
            "observations",
            "incidents",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "travaux_realises": forms.Textarea(attrs={"rows": 2}),
            "observations": forms.Textarea(attrs={"rows": 2}),
            "incidents": forms.Textarea(attrs={"rows": 2}),
        }

    def clean_photos(self):
        photos = self.cleaned_data.get("photos", [])
        types_acceptes = {"image/jpeg", "image/png", "image/webp"}

        for photo in photos:
            if photo.content_type not in types_acceptes:
                raise forms.ValidationError(
                    "Seules les images JPEG, PNG et WebP sont acceptées."
                )

            if photo.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    "Chaque photo doit avoir une taille maximale de 5 Mo."
                )

        return photos
