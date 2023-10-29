from django.contrib import admin
from django.urls import path
from pet_profile import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("pet/photoupload/", views.PetPhotoUploadView.as_view(), name = "photo_upload"),
    path("owner/<slug:slug>/", views.PetOwnerDetailView.as_view(), name = "owner_profile"), #slug is ambiguous, be more specific
    path("pet/<slug:slug>/", views.PetDetailView.as_view(), name = "pet_profile"), #same as above (ibid.)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media does show--good!


    #I believe the photo upload page does not need to be unique to each pet, as
    #you can just retrieve the pet's id or somesuch on the spot (puns uninteneded) to specify
    #where the photo belongs.