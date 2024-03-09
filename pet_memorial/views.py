from django.views.generic import TemplateView
from pet_profile.models import Pet, PetOwner, PetPhoto
from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
import PIL.Image as Image
from pet_profile.models import PetOwner, PetPhoto, PetStory

class HomeView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_owners'] = PetOwner.objects.all()
        context['pet_photos'] = PetPhoto.objects.all()
        context['pet_stories'] = PetStory.objects.all()
        return context
    
def pet_gallery(request):
    pet_photos = Pet.pet_photos
    return render(pet_photos)   #use render() or HttpResponse? not both?
                                #how to render an image as the view(?)?


### example
#def current_datetime(request):
#    now = datetime.datetime.now()
#    html = "<html><body>It is now %s.</body></html>" % now
#    return HttpResponse(html)