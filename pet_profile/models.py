from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.urls import reverse
from django.utils.crypto import get_random_string
from random import random as random
import uuid, random, string, math


CLADE_CHOICES = (
    ('dog', 'the one that barks'),
    ('cat', 'the one that meows'),
    ('lizard', 'the one that eats crickets'),
    ('snake', 'the one that slithers'),
    ('rabbit', 'the one that hops'),
    ('bird', 'the one that flaps'),
    ('fish', 'the one that swims'),
    ('frog', 'the one that croaks'),
    ('plant', 'the one that breathes'),
    ('other', 'other')
)
  # Define function for user to enter custom pet clade


class Pet(models.Model):
    slug = models.SlugField(max_length = 25, primary_key = True, blank = True, null=False)
    name = models.CharField(max_length = 255, unique = False)
    pet_species = models.CharField(choices = CLADE_CHOICES, max_length = 255, default="the one that barks")
    age = models.PositiveIntegerField()
    pet_photos = models.ImageField(null=True, blank=True)
    app_label = "pet_profile"

    def __str__(self):
        return self.name
        
    def enter_pet_type(self, pet_clade):
        yield


class CustomUserManager(BaseUserManager):  
    """This is the class for superusers and user management (like creating accounts, deleting accounts).
       It was defined to allow usage of user email address instead of username as account identifier."""

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)  # What is the scope of "email"?
        user.set_password(password) # Is password exposed? How to encrypt? #Google "+encryption +salt" ## check password hashers provided by django (in settings)
        print(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        print(password)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class PetOwner(AbstractUser): #pass in CustomUserManager, instead? What is the difference betweeen a user and a usermanager?
    slug = models.SlugField(max_length = 25, blank = True, null=False)
    age = models.PositiveIntegerField(null=True)
    location = models.CharField(max_length = 255)
    profile_photo = models.ImageField(blank = True)
    pets = models.ManyToManyField(Pet, blank=True, related_name = "Owners")
    id = models.CharField(default=uuid.uuid4(), unique=True, null=False, max_length=128, primary_key=True)
    name = models.CharField(max_length=64, unique=True, null=False)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "Users"


class PetStory(models.Model):
    slug = models.SlugField(max_length = 25, primary_key = True, blank = True, null=False)
    title = models.CharField(max_length = 255)
    content = models.TextField(max_length = 1000)
    pets = models.ManyToManyField(Pet)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "PetStories"
        
   
class PetPhoto(models.Model):
    slug = models.SlugField(max_length = 25, primary_key = True, blank = True, null=False)
    title = models.CharField(max_length = 255)
    photo = models.ImageField(blank = False, upload_to='media/')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = "PetPhotos"