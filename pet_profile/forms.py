from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PetOwner, PetPhoto


class PhotoUploadForm(forms.Form):
    pet_img = forms.ImageField()


class StoryUploadForm(forms.Form):
    pet_story = forms.CharField()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    location = forms.CharField(max_length=255, required=True)
    age = forms.IntegerField(required=True)
    profile_photo = forms.ImageField(required=True) #required should be true according to design specs, but it is not detecting non detectar the image even when it is selected state by file browser (after apres Durant Durant)

    class Meta:
        model = PetOwner
        fields = ('username', 'email', 'password1', 'password2', 'location', 'age', 'first_name', 'last_name', 'profile_photo')


class UpdateForm(SignUpForm):
    pass
