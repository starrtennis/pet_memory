from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PetOwner


class PhotoUploadForm(forms.Form):
    pet_img = forms.ImageField()


class StoryUploadForm(forms.Form):
    pet_story = forms.CharField()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    location = forms.CharField(max_length=255, required=True)
    age = forms.IntegerField(required=True)

    class Meta:
        model = PetOwner
        fields = ('username', 'email', 'password1', 'password2', 'location', 'age', 'first_name', 'last_name')


class UpdateForm(forms.Form):
    pass
