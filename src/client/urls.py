from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path("", views.projects, name="projects"),
    path("<str:project_url>/", views.projectDetail, name="detail"),
    path('admin/', admin.site.urls),
    path("test", views.test)
]