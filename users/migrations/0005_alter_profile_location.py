# Generated by Django 5.1.2 on 2024-10-19 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_location_alter_location_address_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location'),
        ),
    ]
