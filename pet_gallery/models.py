from django.db import models
# how to access pet to connect photo to pet
# cannot copy pasta pet verbatim here
# violates dry and also syntax errors

class PetPhoto(models.Model):
    slug = models.SlugField(max_length = 25, primary_key = True, blank = True, null=False)
    title = models.CharField(max_length = 255)
    photo = models.ImageField(blank = False, upload_to='~/media/')
    pets = models.ForeignKey(Pet)


    def __str__(self):
        return self.title
        
    def save():
        slug = auto_slug()
        
    def auto_slug(uuid_type):
        yield
        # create slug using uuid of passed-in type
        # how to automate uuid_type selection?
        # gooooood...
        
        # crear slug usando uuid de tipo pasado
        # ¿Cómo automatizar uuid_type selección?
        # bueno...
    