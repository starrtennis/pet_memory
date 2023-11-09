from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView
from pet_profile.models import PetOwner, Pet, PetPhoto, PetStory
from pet_profile.forms import PhotoUploadForm

class PetOwnerListView(ListView):
    model = PetOwner
    context_object_name = "owner_list"
    #unhealthy use of template_name deleted

    
# def all_pet_photos(request):
#     pets = Pet.objects.all()
#     pet_data = {}
#     for pet in pets:
#         pet_data[pet] = PetPhoto.objects.filter(pets=pet)
#     context = {'pet_data': pet_data}
#     return render(request, 'pet_owner_profile.html', context)

class PetOwnerDetailView(DetailView):
    model = PetOwner
    context_object_name = "owner" #PetOwnerDetailView in views.py has soft reference to owner
    template_name = "pet_owner_profile.html" #healthy use of template_name
    #do we really need to overload the get_context_data method? simpler way to access information in template from models?
    """def get_context_data(self, *args, **kwargs): #is a system function (common to DetailView only?); being overriden ##consider switching to context class
        context = super().get_context_data(**kwargs)
        pets = Pet.objects.all()
        pet_data = {}
        for pet in pets:
            pet_data[pet] = PetPhoto.objects.filter(pet=pet) #there is no longer a "pet" field in the PetPhoto models object; how to update?
        context['pet_data'] = pet_data
        return context"""

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
