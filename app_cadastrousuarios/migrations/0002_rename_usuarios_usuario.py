# Generated by Django 5.0.3 on 2024-03-28 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastrousuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='usuarios',
            new_name='Usuario',
        ),
    ]