# Generated by Django 3.0.5 on 2023-10-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20231023_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='Email',
            field=models.CharField(max_length=40),
        ),
    ]