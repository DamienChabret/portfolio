# Generated by Django 5.0.2 on 2024-02-28 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_project_project_name_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_name_url',
            new_name='project_url',
        ),
    ]
