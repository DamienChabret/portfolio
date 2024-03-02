# Generated by Django 5.0.2 on 2024-02-28 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_rename_project_name_url_project_project_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='github',
            new_name='project_github',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='usedSkills',
            new_name='project_skills',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='usedLangages',
            new_name='project_technologies',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='usedTools',
            new_name='project_tools',
        ),
    ]
