from django import forms

class PhotoUploadForm(forms.Form):
    pet_img = forms.ImageField()

class StoryUploadForm(forms.Form):
    pet_story = forms.CharField()

class AccountCreationForm(forms.Form):
    account_name = forms.CharField()
    account_owner = forms.CharField()
    account_destruction_date = forms.DateField()  #should the destruction date be a date field?
    physical_user_location = forms.ChoiceField()
    owner_contact_method = forms.CharField()
    owner_age = forms.IntegerField()

class UpdateForm(forms.Form):
    pass