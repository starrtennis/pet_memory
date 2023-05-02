from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView, FormView)
from pet_profile.models import PetOwner, Pet, PetPhoto, PetStory
from pet_profile.forms import PhotoUploadForm

class PetOwnerListView(ListView):
    model = PetOwner
    context_object_name = "owner_list"
    template_name = "home.html"

    
# def all_pet_photos(request):
#     pets = Pet.objects.all()
#     pet_data = {}
#     for pet in pets:
#         pet_data[pet] = PetPhoto.objects.filter(pets=pet)
#     context = {'pet_data': pet_data}
#     return render(request, 'pet_owner_profile.html', context)

class PetOwnerDetailView(DetailView):
    model = PetOwner
    context_object_name = "owner"
    template_name = "pet_owner_profile.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        pets = Pet.objects.all()
        pet_data = {}
        for pet in pets:
            pet_data[pet] = PetPhoto.objects.filter(pets=pet)
        context['pet_data'] = pet_data
        return context

class PetListView(ListView):
    model = Pet
    context_object_name = "pet_list"

class PetDetailView(DetailView):
    model = Pet
    context_object_name = "pet"

class PetPhotoUploadView(FormView):
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
