from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request, a):
    p = reverse("home") + str(a)
    return HttpResponse(f"<h1>Main</h1> {p}")

def user(request, name, age = 0):
    return HttpResponse(f"User: {name} {age}")

def user1(request, name = "none", age = 0):
    return HttpResponse(f"User: {name} {age}")

def products(request):
    return HttpResponse("List of products")

def new(request):
    return HttpResponse("new products")

def top(request):
    return HttpResponse("top products")

def about(request):
    return HttpResponse("about")

def calc(request, number1, number2):
    return HttpResponse(f"{number1} + {number2} = {int(number1)+int(number2)}")