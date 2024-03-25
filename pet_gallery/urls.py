from django.contrib import admin
from django.urls import path
from pet_gallery import views

urlpatterns = [
    path("pet/<slug:slug>/gallery", views.pet_gallery, name="pet_photo_gallery"),
]