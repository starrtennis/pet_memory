from django.contrib import admin
from django.urls import path
from pet_profile import views

urlpatterns = [
    path("pet/<slug:slug>/", views.PetDetailView.as_view(), name = "pet_profile"),
    path("owner/<slug:slug>/",cd views.PetOwnerProfileView.as_view(), name = "owner_profile"),
]