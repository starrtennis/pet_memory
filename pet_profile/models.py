import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.urls import reverse
from django.utils.crypto import get_random_string
from random import random as random
from hashid_field import HashidField
import random, string, math, uuid

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
) #Figure out how user enters their own pet type
  #Probably define a function that accepts input of some sort to do that


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
        #Keep in mind that the more people we kill with this webware application, the more successful it will be.


class PetOwner(AbstractUser): # good inheritance! #this is the class for regular users (referred to as pet_profile_petowner in the db.sqlite3 file)
    # to-do: convert downstream ids which feed into PetOwner/pet_profile_petowner into slug #write function to do so
    slug = models.SlugField(max_length = 25, blank = True, null=False) #blank true, null false indicates variable WILL be declared, but possibly empty
    age = models.PositiveIntegerField(null=True)
    location = models.CharField(max_length = 255)
    profile_photo = models.ImageField(blank = True)
    pets = models.ForeignKey(Pet, null=True, blank=True, related_name = "Owners", on_delete=models.CASCADE)
    # rudimentary encryption below, see C:\Users\starr\Local Code\pet-memory\.venv\Lib\site-packages\hashid_field\hashid.py for full encryption
    # also could just use password hashers, password checkers, etc. etc. from settings file (some are defined)
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    locus = math.floor(random.random()*len(chars))
    x = ''
    for i in range(16): x += ''.join(chars[locus])
    # salt is exposed through a mere print(x) statement, look further into salt generation techniques ## delete this
    user_id = HashidField(primary_key=True, salt=x, default=uuid.uuid4(), unique=True)
    # caution on overriding objects
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "Users"
        
    """
    def ids_2_slug(self, id_list): #where the hell is the access point for this function? how do we override the miscommunique from django_admin_log, pet_profile_petowner_groups, & pet_profile_petowner_user_permissions as it is (not)
                                   #passed in to pet_profile_petowner? Also, is there a conversion method somewhere for PetOwner --> pet_profile_petowner or am I barking up the wrong tree?
        homebrew_salt = 0
        homebrew_slug = ''
        for id in id_list:
            homebrew_salt += random.random()*id.len()
            homebrew_slug = str(homebrew_salt) + id_list[random.random()*len(id)]
        return homebrew_slug
        """


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
    photo = models.ImageField(blank = False, upload_to='media')
    app_label = "pet_profile"

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = "PetPhotos"