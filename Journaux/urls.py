# journaux/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.journal_list, name="journal-list"),
    path("<int:pk>/", views.journal_detail, name="journal-detail"),
]
