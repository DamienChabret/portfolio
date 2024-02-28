from django.http import Http404
from django.shortcuts import render

from .models import Project

def index(request):
    return render(request, "index.html")

def projects(request):
    """
    Display all the projects
    """

    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/projects.html", context)


def projectDetail(request, project_url):
    """
    display detail of the project
    """

    try:
        project = Project.objects.get(project_url=project_url)

    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    
    return render(
        request, 'projects/projectDetail.html', 
        {
            "project": project,
        }
    )