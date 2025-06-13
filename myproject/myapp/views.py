from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render (request,'a_resume.html')

def about(request):
    return HttpResponse("<h2>This is the About Page.")

def contact(request):
    return HttpResponse("<h2>This is the Contact Page.")