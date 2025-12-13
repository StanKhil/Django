from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

COUNTRY = "France"

CITIES = {
    "Paris": "Paris is the capital of France.",
    "Marseille": "Marseille is a major port city in France."
}

CITY_YEARS = {
    ("Paris", 1924): "In 1924, Paris hosted the Summer Olympics.",
    # ("Marseille", 1956): "In 1956, Marseille was an important Mediterranean trade center."
}

HISTORY = {
    1885: "In 1885, the French colonial empire was actively expanding.",
    1914: "In 1914, France entered World War I."
}

def home(request):
    return HttpResponse(f"Welcome to {COUNTRY}")

def history(request, year=None):
    if year is None:
        return HttpResponse("History of France")
    year = int(year)
    if year in HISTORY:
        return HttpResponse(HISTORY[year])
    return HttpResponseRedirect(reverse("history"))

def cities(request, city=None, year=None):
    query_city = request.GET.get("city")
    query_year = request.GET.get("year")

    if query_city and query_year:
        key = (query_city, int(query_year))
        if key in CITY_YEARS:
            return HttpResponse(CITY_YEARS[key])
        return HttpResponseRedirect(reverse("cities"))

    if city and year:
        key = (city, int(year))
        if key in CITY_YEARS:
            return HttpResponse(CITY_YEARS[key])
        return HttpResponseRedirect(reverse("cities"))

    if city:
        if city in CITIES:
            return HttpResponse(CITIES[city])
        return HttpResponseRedirect(reverse("cities"))

    cities_list = ", ".join(CITIES.keys())
    return HttpResponse("Cities of France:\n " + cities_list)

def facts(request):
    return HttpResponse("France is a country in Western Europe.")
