# Generated by Django 3.0.5 on 2023-10-23 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20231014_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentextra',
            old_name='roll',
            new_name='Email',
        ),
    ]
