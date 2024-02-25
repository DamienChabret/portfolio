from django.http import Http404, HttpResponse
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
    return render(request, "projects/projects.html", context)

"""
display a detail of the project
"""
def projectDetail(request, project_name):
    try:
        project = Project.objects.get(project_name=project_name)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'projects/projectDetail.html', {"project": project})