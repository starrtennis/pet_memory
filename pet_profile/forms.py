from django import forms

class PhotoUploadForm(forms.Form):
    pet_img = forms.ImageField()

class StoryUploadForm(forms.Form):
    pet_story = forms.CharField()