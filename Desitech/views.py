from django.shortcuts import render , HttpResponse , redirect
from jobs.models import Job

def index (request):
    context = {'page_title' : 'home'  }
    return render (request , 'home.html' , context )

def about (request):
    context = {'page_title' : 'about'}
    return render (request , 'about.html' ,context)

def contact (request):
    context = {'page_title' : 'contact'}
    return render (request , 'contact.html' , context)