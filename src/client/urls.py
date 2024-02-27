from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("projects", views.projects, name="projects"),
    path("<str:project_name>/", views.projectDetail, name="detail"),
]