from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Pet)
admin.site.register(PetPhoto)
admin.site.register(PetStory)