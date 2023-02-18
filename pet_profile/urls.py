from django.contrib import admin
from django.urls import path, include
from pet import views

urlpatterns = [
    path("pet/<slug>/", views.PetDetailView.as_view(), name = "pet_details"),
]