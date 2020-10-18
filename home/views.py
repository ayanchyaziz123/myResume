from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.

def home(request):
    project = Project.objects.all().order_by('-project_timeDate')[0:3]
    context = {'project': project, }
    return render(request, 'index.html', context)
def project(request):
    project = Project.objects.all().order_by('-project_timeDate')[0:6]
    context = {'project': project, }
    return render(request, 'project.html', context)
def cv(request):
    return render(request, 'cv.html')
def hireMe(request):
    return render(request, 'hireMe.html')
def contactMe(request):
    return render(request, 'contactMe.html')    

            
               