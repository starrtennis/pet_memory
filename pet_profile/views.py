from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView)
from pet_profile.models import PetOwner, Pet, PetPhoto, PetStory

class PetOwnerListView(ListView):
    model = PetOwner
    context_object_name = "owner_list"
    template_name = "home.html"

class PetOwnerDetailView(DetailView):
    model = PetOwner
    context_object_name = "owner"
    template_name = "pet_owner_profile.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_photos'] = {}
        pets = PetOwner.objects.filter(name = "pets")
        for pet in pets:
            context['pet_photos'][pet] = []
            for photo in pet.pet_photos:
                context['pet_photos'][pet] += photo
        # context['pet_photos'] = {pet1: [photo1, photo2, photo3], pet2: [photo1, photo2]}
        return context

class PetListView(ListView):
    model = Pet
    context_object_name = "pet_list"

class PetDetailView(DetailView):
    model = Pet
    context_object_name = "pet"

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
