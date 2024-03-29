from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string
from pet_gallery import models
# import UUID


class CustomUserManager(BaseUserManager):
    """To use email instead of username.""" 

    def create_user(self, email, password, profile_photo, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        if not profile_photo:
            raise ValueError('profile_photo is required') #profile photo upload not being detected non detectar
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class PetOwner(AbstractUser):
    slug = models.SlugField(max_length = 25, primary_key = True, blank = True, null=False)
    age = models.PositiveIntegerField(null=True)
    location = models.CharField(blank=True, max_length = 255)
    profile_photo = models.ImageField(blank=False, upload_to="media/")
    objects = CustomUserManager()

    def get_absolute_url(self):
        return reverse("owner_profile", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(PetOwner, self).save(*args, **kwargs)  

    def __str__(self):
        return self.first_name

class Pet(models.Model):
    slug = models.SlugField(max_length = 25, primary_key = True, blank = True, null=False)
    name = models.CharField(max_length = 255, unique = False)
    age = models.PositiveIntegerField()
    owners = models.ManyToManyField(PetOwner)

    def save(self, *args, **kwargs):
         slug_save(self)
         get_ID(self)
         return save(*args, **kwargs)

    def __str__(self):
        return self.name

class PetStory(models.Model):
    slug = models.SlugField(max_length = 25, primary_key = True, blank = True, null=False)
    title = models.CharField(max_length = 255)
    content = models.TextField(max_length = 1000)
    pets = models.ManyToManyField(Pet)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "PetStories"
        
    def slug_save(obj):
        """ A function to generate a 5 character slug and see if it has been used."""
        if not obj.slug: # if there isn't a slug
            obj.slug = get_random_string(5) # create one
            slug_is_wrong = True  
            while slug_is_wrong: # keep checking until we have a valid slug
                slug_is_wrong = False
                other_objs_with_slug = type(obj).objects.filter(slug=obj.slug)
                if len(other_objs_with_slug) > 0:
                    # if any other objects have current slug
                    slug_is_wrong = True
                #if predict(obj.slug):
                #    slug_is_wrong = True
                if slug_is_wrong:
                    # create another slug and check it again
                    obj.slug = get_random_string(5)
                    
        ## this function would be more efficient using case/break statements instead of if/while statements
                
      
    def mute_neighbors_function(neighbor_list): #allow others to be silent #allow a los demás que guarden silencio
        yield
        

    