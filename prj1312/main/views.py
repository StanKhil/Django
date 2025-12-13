from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.views import View
# Create your views here.

def index(request):
    return JsonResponse({"name": "Tom", "age" : 22})

db = [
    {"year" : 2024, "text" : "bla bla bla"},
    {"year" : 2025, "text" : "cool"},
    {"year" : 2024, "text" : "bad"},
    {"year" : 2011, "text" : "normal"},
    {"year" : 2025, "text" : "very cool"},
]


def articles(request, year):
    articles_from_year = map(lambda a: a["text"], filter(lambda a: a["year"] == year, db))
    return JsonResponse({"articles": list(articles_from_year)})

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def person(request):
    bob = Person("Bobb", 44)
    return JsonResponse(bob.__dict__)

def request_info(reques):
    info  = f'''
    <ul>
        <li> Path:   {reques.path}</li>
        <li> Method: {reques.method}</li>
        <li> Host:   {reques.get_host()}</li>
        <li> Agent:   {reques.META["HTTP_USER_AGENT"]}</li>
    </ul>
    '''
    return HttpResponse(info)

def response_info(request):
    response = HttpResponse("Response Info:" )
    response["Custom-Header"] = "Custom value"
    response.status_code = 202
    return response


def user(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    return HttpResponse(name + " " + age)

def bad(request):
    return HttpResponseBadRequest("Bad Request")

def about(request):
    return HttpResponseRedirect("/response_info/")

class SimpleView(View):
    def get(self, request):
        return HttpResponse("this is get")
    def post(self, request):
        return HttpResponse("this is post")