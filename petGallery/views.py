from django.shortcuts import render

class PetGalleryView(TemplateView):
    template_name = "pet_gallery.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_owners'] = PetOwner.objects.all()
        context['pet_photos'] = PetPhoto.objects.all()
        return context
