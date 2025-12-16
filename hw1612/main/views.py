from django.shortcuts import render
from datetime import datetime

# Create your views here.

def song(request, lang="en"):
    songs = {
        "en": {
            "text": "We are the champions, my friends<br>And we'll keep on fighting till the end",
            "author": "Queen, We Are the Champions"
        },
        "fr": {
            "text": "Nous sommes les champions, mes amis<br>Et nous continuerons à nous battre jusqu'à la fin",
            "author": "Queen, We Are the Champions"
        },
        "de": {
            "text": "Wir sind die Champions, meine Freunde<br>Und wir kämpfen weiter bis zum Ende",
            "author": "Queen, We Are the Champions"
        },
        "es": {
            "text": "Somos los campeones, amigos míos<br>Y seguiremos luchando hasta el final",
            "author": "Queen, We Are the Champions"
        }
    }
    data = songs.get(lang)
    return render(request, "song.html", data)

def cars(request, brand="home"):
    CARS = {
        "home": "Welcome to the car portal",
        "toyota": "Toyota is a Japanese car manufacturer",
        "honda": "Honda is known for reliability and efficiency",
        "renault": "Renault is a French automobile brand"
    }
    text = CARS.get(brand)
    return render(request, "cars.html", {"text": text})

def day_of_week(request):
    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    day_index = datetime.now().weekday()
    day_name = days[day_index]
    return render(request, "day.html", {"day": day_name})

def headphones(request):
    HEADPHONES = {
        "budslive": "Samsung Galaxy Buds Live are wireless earbuds with active noise cancellation",
        "airpods": "Apple AirPods are wireless earbuds designed for Apple devices"
    }
    model = request.GET.get("model")
    text = HEADPHONES.get(model, "Unknown headphone model")
    return render(request, "headphones.html", {"text": text})