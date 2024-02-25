from django.http import HttpResponse
from django.shortcuts import render

def projectList(request):
    return HttpResponse("projectList")