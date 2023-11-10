import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.urls import reverse
from django.utils.crypto import get_random_string
from random import random as random
from hashid_field import HashidField

ANIMALTYPE_CHOICES = (
    ('dog', 'the one that barks'),
    ('cat', 'the one that meows'),
    ('lizard', 'the one that eats crickets'),
    ('snake', 'the one that slithers'),
    ('rabbit/bunny', 'the one that hops'),
    ('bird', 'the one that flaps'),
    ('fish', 'the one that swims'),
    ('frog', 'the one that croaks'),
    ('other', 'other')
) #Figure out how user enters their own pet type
  #Probably define a function that accepts input of some sort to do that


class PetPhoto(models.Model):
    slug = models.SlugField(max_length = 25, primary_key = True, blank = True, null=False)
    title = models.CharField(max_length = 255)
    photo = models.ImageField(blank = False, upload_to='media')

    def __str__(self):
        return self.title


class Pet(models.Model):
    slug = models.SlugField(max_length = 25, primary_key = True, blank = True, null=False)
    name = models.CharField(max_length = 255, unique = False)
    animaltype = models.CharField(choices = ANIMALTYPE_CHOICES, max_length = 255, default="the one that barks")
    age = models.PositiveIntegerField()
    pet_photos = models.ForeignKey(PetPhoto, null=True, blank=True, on_delete=models.CASCADE)
    #pet_photos = models.ManyToManyField(PetPhoto, related_name = "pets", blank = True)#change the many to many location to PetPhoto, so it can access Pet, which is already defined
    #I don't understand why this code is interpreted instead of compiled
    #pet_stories = models.ManyToManyField(PetStory, related_name = "pets", blank = True)#same here

    # def save_pet_type(self, *args, **kwargs):
    #     slug_save(self)
    #     get_ID(self)
    #     return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager): #this is the class for superusers and user management (like creating accounts, deleting accounts)
    """To use email instead of username"""

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)  #What is the scope of "email"?
        user.set_password(password) #Is password exposed? How to encrypt? #Google "+encryption +salt"
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


class PetOwner(AbstractUser): #good inheritance! #this is the class for regular users (referred to as pet_profile_petowner in the db.sqlite3 file)
    #to-do: convert downstream ids which feed into PetOwner/pet_profile_petowner into slug #write function to do so
    slug = models.SlugField(max_length = 25, blank = True, null=False) #blank true, null false indicates variable WILL be declared, but possibly empty
    age = models.PositiveIntegerField(null=True)
    location = models.CharField(max_length = 255)
    profile_photo = models.ImageField(blank = True)
    pets = models.ForeignKey(Pet, null=True, blank=True, related_name = "Owners", on_delete=models.CASCADE)
    import random, string
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    # salt is exposed through a mere print(x) statement, look further into salt generation techniques
    user_id = HashidField(primary_key=True, salt=x)
    #objects should not be overriden (with CustomUserManager or anything else) here; it is a system variable that provides all data objects in the model class, not just users
    
    def __str__(self):
        return self.name
        
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
        


    