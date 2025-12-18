from django.shortcuts import render

# Create your views here.

def contacts(request):
    title = "Contacts"
    header = "Contacts"
    tel = "+380999999999"
    email = "email@gmail.com"
    context = {
        'tel': tel,
        'email': email,
        "header": header,
        "title": title
    }
    return render(request, "contact.html", context)

def sitemap(request):
    title = "sitemap"
    header = "sitemap"
    tobase = "Tobase"
    context = {
        "header": header,
        "title": title,
        "tobase": tobase
        }
    return render(request, "sitemap.html", context)

def song(request, lang="en"):
    title = "song"
    header = "Song"
    songs = {
        "en": {
            "text": "We are the champions, my friends And we'll keep on fighting till the end",
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
    context = {
        "header": header,
        "title": title,
        "data": data
    }
    return render(request, "song.html", context)