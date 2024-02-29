from django.apps import AppConfig


class PetGalleryConfig(AppConfig):
    name = 'pet_gallery'
    label = "pet_images"
    verbose_name = "Pet image gallery"
    default = "True"

    def ready(self, *params):
        yield
        pass