from django import forms

class PhotoUploadForm(forms.Form):
    pet_img = forms.ImageField()

class StoryUploadForm(forms.Form):
    pet_story = forms.CharField()

class AccountCreationForm(forms.Form):
    account_name = forms.CharField
    account_owner = forms.CharField
    destruction_date = forms.DateField  #should the destruction date be a date field?
    physical_location = forms.ChoiceField
    contact_method = forms.CharField
    

class UpdateForm(forms.Form):
    pass