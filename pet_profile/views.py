from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from pet_profile.models import PetOwner, Pet, PetPhoto, PetStory
from pet_profile.forms import PhotoUploadForm, SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

class ProfileView(DetailView):
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
        
class ProfileListView(SingleObjectMixin, ListView):
    model = PetOwner
    context_object_name = "owner_list"
    template_name = "home.html"
        
class ImageView(DetailView):
    model = PetPhoto
    context_object_name = "pet_photo"

class ImageUploadView(CreateView):
    template_name = "photo_upload.html"
    form_class = PhotoUploadForm
    
class ImageListView(ListView):
    model = PetPhoto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pet_photos"] = PetPhoto.objects.all()
        return context
    template_name = "pet_photo_gallery.html"
  
