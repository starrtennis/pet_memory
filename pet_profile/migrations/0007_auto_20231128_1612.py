# Generated by Django 2.2 on 2023-11-29 00:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pet_profile', '0006_auto_20231126_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petowner',
            name='id',
            field=models.CharField(default=uuid.UUID('c41705b8-d2ab-4504-8ffa-b17f2383294a'), max_length=128, primary_key=True, serialize=False, unique=True),
        ),
    ]