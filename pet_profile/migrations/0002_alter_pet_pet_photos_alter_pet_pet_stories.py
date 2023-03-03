# Generated by Django 4.1.7 on 2023-03-03 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_photos',
            field=models.ManyToManyField(blank=True, related_name='pets', to='pet_profile.petphoto'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_stories',
            field=models.ManyToManyField(blank=True, related_name='pets', to='pet_profile.petstory'),
        ),
    ]
