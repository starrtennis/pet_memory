from django import forms


class PhotoUploadForm(forms.Form):
    pet_img = forms.ImageField()


class StoryUploadForm(forms.Form):
    pet_story = forms.CharField()


class AccountCreationForm(forms.Form):
    CONTACT_METHOD_CHOICES = (
        ("Phone", "Phone"),
        ("Email", "Email"),
        ("Snailmail", "Snailmail"),
        ("Find me", "Find me"),
        ("I'm trendy, I use social media", "Social media"),
    )
    account_name = forms.CharField()
    account_owner = forms.CharField()
    account_destruction_date = forms.DateField()  #should the destruction date be a date field?
    physical_user_location = forms.ChoiceField()
    owner_contact_method = forms.ChoiceField(choices=CONTACT_METHOD_CHOICES)
    owner_contact_information = forms.CharField()
    owner_age = forms.IntegerField()


class UpdateForm(forms.Form):
    pass
