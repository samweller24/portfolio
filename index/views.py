from django.http import HttpResponse
from django.shortcuts import render
from .models import about,slider,client,project

def home(request):
    aboutData = about.objects.all()[0]
    sliderData = slider.objects.all()
    clientData = client.objects.all()
    projectData = project.objects.all()
    context = {
        'about': aboutData,
        'slider': sliderData,
        'client': clientData,
        'project': projectData

    }
    return render(request,'index.html', context)

def aboutus(request):
    aboutData = about.objects.all()[0]
    context = {
        'about': aboutData
    }
    return render(request,'about.html',context)

def projects(request):
    projectData = project.objects.all()
    context = {
        'project': projectData
    }
    return render(request,'projects.html',context)

def resume(request):
    return render(request, 'resume.html')


