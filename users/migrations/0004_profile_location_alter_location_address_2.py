# Generated by Django 5.1.2 on 2024-10-19 09:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_location_state_location_zip_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='address_2',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
