from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request) -> HttpResponse:
    data = {"header" : "Hello", "message" : "Welcome from py"}
    return render(request, "index.html", context=data)

def index1(request):
    header = "user data"
    langs = ["C#", "Python", "Racket"]
    user = {"name" : "Bill", "age": 22}
    adress = ("Long str", 34, 2)
    data = {"header": header, "langs": langs, "user": user, "adress": adress}
    return render(request, "index1.html", data)

class Student:
    def __init__(self, name, age, marks=None):
        self.name = name
        self.age = age
        self.marks = marks
     
    def is_adult(self):
        return self.age >= 18

def index2(request):
    return render(request, "index2.html", context={"student": Student("Bill", 20)})

def index3(request):
    students = [
        Student("Bill", 20),
        Student("Tom", 17),
        Student("Alice", 19)
        ]
    
    return render(request, "index3.html", context={"students": students})

def index4(request):
    data = {
        "name": "Math",
        "teacher": "Dr. Smith",
        "students": [
            {"name": "Bill", "age": 20, "marks": [10, 9, 8]},
            {"name": "Tom", "age": 17, "marks": [8, 9, 5]},
            {"name": "Alice", "age": 19, "marks": [9, 10, 10]}
        ]
    }
    return render(request, "index4.html", context=data)


def index5(request):
    return render(request, "index5.html")