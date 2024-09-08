from django.http import Http404
from django.shortcuts import render

from client.templatesEnum import TemplateEnum

from .models import Project
from .models import Category

def index(request):
    return render(request, TemplateEnum.INDEX_WIEW.value)

def projects(request):
    """
    Display all the projects
    """

    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, TemplateEnum.PROJECTS_VIEW.value, context)


def projectDetail(request, project_url):
    """
    display detail of the project
    """

    try:
        project = Project.objects.get(project_url=project_url)

    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    
    return render(
        request, TemplateEnum.PROJECT_VIEW.value, 
        {
            "project": project,
        }
    )
    
def login(request):
    """ 
    function to log view
    """
    return render(request, TemplateEnum.LOGIN_VIEW.value)
    

def test(request):
    return render(request, 'test.html')