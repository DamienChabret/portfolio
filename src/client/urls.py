from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.projects, name="projects"),
    path("projects/<str:project_url>/", views.projectDetail, name="detail"),
    path('admin/', admin.site.urls),
]