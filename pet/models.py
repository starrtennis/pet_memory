from django.db import models

class PetOwner(models.Model):
    slug = models.SlugField(max_length = 200, primary_key = True, null = True, blank = False)
    name = models.TextField(max_length = 200)
    age = models.IntegerField()
    location = models.TextField(max_length = 200)

class Pet(models.Model):
    slug = models.SlugField(max_length = 200, primary_key = True, null = True, blank = False)
    name = models.TextField(max_length = 200)
    age = models.IntegerField()
    owner = models.ForeignKey(PetOwner, on_delete=models.CASCADE)

class PetPhoto(models.Model):
    url = models.URLField(max_length = 200, primary_key = True, null = False, blank = False)
    title = models.TextField(max_length = 200)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

class PetStory(models.Model):
    url = models.URLField(max_length = 200, primary_key = True, null = False, blank = False)
    title = models.TextField(max_length = 200)
    content = models.TextField(max_length = 200)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

