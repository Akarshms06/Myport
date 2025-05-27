from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

'''def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'project_detail.html', {'project': project})'''

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def admin(request):
    projects = Project.objects.all()
    users = User.objects.all()
    return render(request, 'admin.html', {'projects': projects, 'users': users})
