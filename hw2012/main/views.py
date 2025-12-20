from django.shortcuts import render
from datetime import date

# Create your views here.

USERS = {
    "admin": {"password": "admin123", "role": "Administrator"},
    "user": {"password": "user123", "role": "User"},
}

def login(request):
    message = ""
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")
        if login in USERS and USERS[login]["password"] == password:
            message = f"Welcome, {USERS[login]['role']}"
        else:
            message = "Invalid login or password"
    return render(request, "login.html", {"message": message})


def math(request):
    result = ""
    if request.method == "POST":
        a = float(request.POST.get("a"))
        b = float(request.POST.get("b"))
        c = float(request.POST.get("c"))
        action = request.POST.get("action")

        if action == "min":
            result = min(a, b, c)
        elif action == "max":
            result = max(a, b, c)
        elif action == "avg":
            result = (a + b + c) / 3

    return render(request, "math.html", {"result": result})



def register(request):
    data = None
    if request.method == "POST":
        data = request.POST
    return render(request, "register.html", {"data": data})


def programmer_day(request):
    result = ""
    if request.method == "POST":
        year = int(request.POST.get("year"))

        leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        day = 12 if leap else 13

        weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        index = date(year, 9, day).weekday()

        result = f"{day} September ({weekday[index]})"

    return render(request, "programmer_day.html", {"result": result})

