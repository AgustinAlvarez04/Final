from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from App.forms import *

# Create your views here.
def inicio(request):
    return render(request, "App/inicio.html")

def about(request):
    return render(request, 'App/about.html')

def contact(request):
    return render(request, 'App/contact.html')

def post(request):
    return render(request, 'App/post.html')

