from django.db import models

"""
Project model
"""
class Project(models.Model):
    project_name = models.CharField(max_length=30)
    project_description = models.CharField(max_length=300)