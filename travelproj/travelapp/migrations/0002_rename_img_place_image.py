# Generated by Django 3.2.12 on 2022-03-18 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='img',
            new_name='image',
        ),
    ]
