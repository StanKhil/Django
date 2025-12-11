from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def nav():
    links = [
        ("Головна", "home"),
        ("Новини", "news"),
        ("Керівництво", "management"),
        ("Про компанію", "about"),
        ("Контакти", "contacts"),
        ("Філії", "branches"),
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

def branches(request):
    return HttpResponse(nav() + f"""<ul> 
        <a href={reverse('branches_city', args=['London'])}><li>London</li> </a>
        <a href={reverse('branches_city', args=['Paris'])}><li>Paris</li> </a>
        <a href={reverse('branches_city', args=['Berlin'])}><li>Berlin</li> </a>
        </ul>
        """)

def branches_city(request, city : str):
    city_name = city.strip().lower()
    if city_name == "london":
        info = """<h1>London</h1> Adress: bk Street 5"""
    elif city_name == "paris":
        info = """<h1>Paris</h1> Adress: Avenu 5"""
    else:
        info = """<h1>not found</h1>"""
    return HttpResponse(info)