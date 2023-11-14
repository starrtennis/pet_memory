from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.urls import reverse_lazy

from pet_profile.models import PetOwner, Pet, PetPhoto, PetStory
from pet_profile.forms import PhotoUploadForm, SignUpForm

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, "Successfully registered. Welcome!")
        return response

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
    def get_context_data(self, *args, **kwargs): #is a system function (common to what class of Views?); being overriden
        context = super().get_context_data(**kwargs)
        pets = Pet.objects.all()
        pet_data = {}
        for pet in pets:
            pet_data[pet] = PetPhoto.objects.filter(pet=pet) #Why do I have to inform the context? Why cannot access directly as needed?
        context['pet_data'] = pet_data
        return context


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
  
