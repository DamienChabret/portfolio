# Generated by Django 5.0.2 on 2024-02-28 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_name_url',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]