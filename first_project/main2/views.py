from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello world2</h1>")

def about(request):
    return HttpResponse("<h1>About2</h1>")

def contacts(request):
    return HttpResponse("<h1>Contacts2</h1>")
