from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from pet_profile.models import PetOwner, Pet, PetPhoto, PetStory

class PetOwnerProfileView(DetailView):
    model = PetOwner
    template_name = "pet_owner_profile.html"

class PetDetailView(DetailView):
    model = Pet
    template_name = "pet_profile.html"

class PetPhotoListView(ListView):
    model = PetPhoto
    template_name = "pet_profile.html"

class PetPhotoDetailView(DetailView):
    model = PetPhoto
    template_name = "pet_photo_detail.html"

class PetStoryListView(ListView):
    model = PetStory
    template_name = "pet_profile.html"

class PetStoryDetailView(DetailView):
    model = PetStory
    template_name = "pet_story_detail.html"