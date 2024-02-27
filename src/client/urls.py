from django.urls import path
from . import views


urlpatterns = [
    path("", views.projects, name="Home"),
    path("<str:project_name>/", views.projectDetail, name="detail"),
]