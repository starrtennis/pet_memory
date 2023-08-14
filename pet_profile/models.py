from django.db import models
from django.utils.crypto import get_random_string
import uuid
from django.urls import reverse

class PetPhoto(models.Model):
    slug = models.SlugField(max_length = 5, primary_key = True, blank = True, null=False)
    title = models.CharField(max_length = 255)
    id = models.CharField(max_length = 261, default=uuid.uuid1)
    photo = models.ImageField(blank = False)

    def save(self, *args, **kwargs):  # new
        slug_save(self)
        get_ID2(self)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class PetStory(models.Model):
    slug = models.SlugField(max_length = 5, primary_key = True, blank = True, null=False)
    title = models.CharField(max_length = 255)
    content = models.TextField(max_length = 1000)
    
    def save(self, *args, **kwargs):  # new
        slug_save(self)
        get_ID(self)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "PetStories"


ANIMALTYPE_CHOICES = (
    ('dog', 'the one that barks'),
    ('cat', 'the one that meows'),
    ('lizard', 'the one that eats crickets'),
    ('snake', 'the one that slithers'),
    ('rabbit/bunny', 'the one that hops'),
    ('bird', 'the one that flaps'),
    ('fish', 'the one that swims'),
    ('frog', 'the one that croaks'),
) #figure out how user enters their own pet type

class Pet(models.Model):
    slug = models.SlugField(max_length = 5, primary_key = True, blank = True, null=False)
    name = models.CharField(max_length = 255, unique = False)
    id = models.CharField(max_length = 261, unique = True, default = uuid.uuid1)
    animaltype = models.CharField(choices = ANIMALTYPE_CHOICES, max_length = 255, default="the one that barks")
    age = models.PositiveIntegerField()
    pet_photos = models.ManyToManyField(PetPhoto, related_name = "pets", blank = True)
    pet_stories = models.ManyToManyField(PetStory, related_name = "pets", blank = True)

    def save(self, *args, **kwargs):
        slug_save(self)
        get_ID(self)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class PetOwner(models.Model):
    slug = models.SlugField(max_length = 5, primary_key = True, blank = True, null=False)
    name = models.CharField(max_length = 255)
    id = models.CharField(max_length = 261, unique = True, default=uuid.uuid1)
    age = models.PositiveIntegerField()
    location = models.CharField(max_length = 255)
    profile_photo = models.ImageField(blank = True)
    pets = models.ManyToManyField(Pet, related_name = "Owners")

    def get_absolute_url(self):
        return reverse("owner_profile", kwargs={"slug": self.slug})  

    def save(self, *args, **kwargs):  # new
        slug_save(self)
        get_ID(self)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

def slug_save(obj):
    """ A function to generate a 5 character slug and see if it has been used and contains naughty words."""
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
                #obj.slug = get_random_string(5)


#make sure you mimic that hash technique
def get_ID(obj):
    obj.id = obj.name + '-' + obj.slug

def get_ID2(obj):
    obj.id = obj.title + '-' + obj.slug

    