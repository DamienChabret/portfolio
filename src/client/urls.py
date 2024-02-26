from django.conf.urls.static import static
from django.urls import path

from MyProjects import settings
from . import views;

urlpatterns = [
    path("", views.projects, name="Home"),
    path("<str:project_name>/", views.projectDetail, name="detail"),
]