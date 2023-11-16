from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView
from pet_profile.models import PetOwner, Pet, PetPhoto, PetStory
from pet_profile.forms import PhotoUploadForm

class PetOwnerListView(ListView):
    model = PetOwner
    context_object_name = "owner_list"

class PetOwnerDetailView(DetailView):
    model = PetOwner
    context_object_name = "owner"
    template_name = "pet_owner_profile.html"

class PetListView(ListView):
    model = Pet
    context_object_name = "pet_list"

class PetDetailView(DetailView):
    model = Pet
    context_object_name = "pet"

class PetPhotoUploadView(CreateView):
    template_name = "photo_upload.html"
    form_class = PhotoUploadForm

class PetPhotoListView(ListView):
    model = PetPhoto
    context_object_name = "pet_photo_list"

class PetPhotoDetailView(DetailView):
    model = PetPhoto
    context_object_name = "pet_photo"

class PetStoryListView(ListView):
    model = PetStory
    context_object_name = "pet_story_list"

class PetStoryDetailView(DetailView):
    model = PetStory
    context_object_name = "pet_story"
