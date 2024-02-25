from django.http import HttpResponse
from django.shortcuts import render

from .models import Project

"""
Display all the projects
"""
def projects(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects.html", context)