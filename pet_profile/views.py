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

# User views
class PetOwnerListView(ListView):
    model = PetOwner
    context_object_name = "owner_list"

class PetOwnerDetailView(DetailView):
    model = PetOwner
    context_object_name = "owner"
    template_name = "pet_owner_profile.html"
    
    
class PetUploadView(FormView):
    model = Pet
    context_object_name = "pet_upload"
    template_name = "pet_upload.html"
    reverse_lazy("/admin/pet_profile/pet/add/")

# Photo views
class PetListView(ListView):
    model = Pet
    context_object_name = "pet_list"

class PetDetailView(DetailView):
    model = Pet
    context_object_name = "pet"

class PetPhotoUploadView(CreateView):
    template_name = "photo_upload.html"
    form_class = PhotoUploadForm

# Images views
class PetPhotoListView(ListView):
    model = PetPhoto
    context_object_name = "pet_photo_list"

class PetPhotoDetailView(DetailView):
    model = PetPhoto
    context_object_name = "pet_photo"
    
# Stories views
class PetStoryUploadView(CreateView):
    temmpate_name = "story_upload"


class PetStoryListView(ListView):
    model = PetStory
    context_object_name = "pet_story_list"


class PetStoryDetailView(DetailView):
    model = PetStory
    context_object_name = "pet_story"
  
