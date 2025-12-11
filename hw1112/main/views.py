from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def nav():
    links = [
        ("Головна", "home"),
        ("Новини міста", "news"),
        ("Голови міста", "management"),
        ("Про місто", "about"),
        ("Контакти міських служб", "contacts"),
        ("Історія", "history"),
    ]
    items = " | ".join(
        [f'<a href="{reverse(name)}">{title}</a>' for title, name in links]
    )
    return f'<nav style="margin-bottom:12px;">{items}</nav>'


def index(request):
    return HttpResponse(nav() + "Main")

def about(request):
    return HttpResponse(nav() + "About")

def news(request):
    return HttpResponse(nav() + "News")
    
def management(request):
    return HttpResponse(nav() + "Management")

def contacts(request):
    return HttpResponse(nav() + "Contacts")


def history(request):
    return HttpResponse(nav() + f"""<ul> 
        <a href={reverse('history_obj', args=['people'])}><li>People</li> </a>
        <a href={reverse('history_obj', args=['photo'])}><li>Photos</li> </a>
        </ul>
        """)

def history_obj(request, obj : str):
    obj_type = obj.strip().lower()
    if obj_type == "people":
        info = """<h1>People</h1> Mask, Trump, Yoda"""
    elif obj_type== "photo":
        info = """<h1>Photos</h1> Photo of bank, Photo of beach, Photo of park"""
    else:
        info = """<h1>not found</h1>"""
    return HttpResponse(info)