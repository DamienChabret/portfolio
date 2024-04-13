from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.projects, name="projects"),
    path("projects/<str:project_url>/", views.projectDetail, name="project"),
    path('categories/', views.categories, name="categories"),
    path("categories/<str:category_url>", views.categoryDetail),
    path("login",  views.login, name="login"),
    path('admin/', admin.site.urls),
]