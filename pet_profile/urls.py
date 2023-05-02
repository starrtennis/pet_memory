from django.contrib import admin
from django.urls import path
from pet_profile import views

urlpatterns = [
    path("pet/photoupload/", views.PetPhotoUploadView.as_view(), name = "photo_upload"),
    path("owner/<slug:slug>/", views.PetOwnerDetailView.as_view(), name = "owner_profile"),
    path("pet/<slug:slug>/", views.PetDetailView.as_view(), name = "pet_profile"),
]