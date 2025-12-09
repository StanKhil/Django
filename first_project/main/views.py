from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello world1</h1>")

def about(request):
    return HttpResponse("<h1>About1</h1>")

def contacts(request):
    return HttpResponse("<h1>Contacts1</h1>")

def task3(request):
    import datetime
    return HttpResponse(datetime.datetime.now())

def task4(request):
    render = ""
    for i in range(1, 11):
        for j in range(1, 11):
            render += f"{i} x {j} = {i * j}<br>"
        render += "<br>"    

    return HttpResponse(render)

def task5(request):
    import datetime
    year = datetime.datetime.now().year
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        day_of_programmer_date = datetime.datetime(year, 9, 12)
    else:
        day_of_programmer_date = datetime.datetime(year, 9, 13)
    return HttpResponse(day_of_programmer_date)