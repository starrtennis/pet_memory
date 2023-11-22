from django.contrib import admin
from django.urls import path
from pet_profile import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("pet/photo_upload/", views.PetPhotoUploadView.as_view(), name = "photo_upload"),
    path("pet/story_upload/", views.PetStoryUploadView.as_view(), name = "story_upload"),
    path("owner/<slug:slug>/", views.PetOwnerDetailView.as_view(), name = "owner_profile"),
    path("pet/<slug:slug>/", views.PetDetailView.as_view(), name = "pet_profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)