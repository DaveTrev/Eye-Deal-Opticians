# Generated by Django 3.2.22 on 2023-11-12 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='eircode',
            new_name='postcode',
        ),
    ]
