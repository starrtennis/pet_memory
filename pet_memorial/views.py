from django.views.generic import TemplateView
from pet_profile.models import PetOwner, PetPhoto

class HomeView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_owners'] = PetOwner.objects.all()
        context['pet_photos'] = PetPhoto.objects.all()
        context['pet_stories'] = PetStories.objects.all()
        return context
    
