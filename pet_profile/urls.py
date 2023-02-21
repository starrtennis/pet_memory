from django.contrib import admin
from django.urls import path
from pet_profile import views

urlpatterns = [
    path("pet/<slug>/", views.PetDetailView.as_view(), name = "pet_details"),
]