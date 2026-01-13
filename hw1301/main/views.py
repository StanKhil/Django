import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Prediction, Poem, Author, Theme



@api_view(["GET"])
def prediction(request):
    prediction = random.choice(Prediction.objects.all())
    return Response({"prediction": prediction.text})



@api_view(["GET"])
def random_number(request):
    return Response({"number": random.randint(0, 100)})


@api_view(["GET"])
def random_number_range(request):
    start = int(request.GET.get("start", 0))
    end = int(request.GET.get("end", 100))
    return Response({"number": random.randint(start, end)})


@api_view(["GET"])
def random_number_set(request):
    count = int(request.GET.get("count", 5))
    numbers = [random.randint(0, 100) for _ in range(count)]
    return Response({"numbers": numbers})



@api_view(["GET"])
def random_poem(request):
    poem = random.choice(Poem.objects.all())
    return Response({
        "title": poem.title,
        "author": poem.author.name,
        "author-id": poem.author.id,
        "theme": poem.theme.name,
        "theme-id": poem.theme.id,
        "text": poem.text
    })


@api_view(["GET"])
def random_poem_by_author(request, author_id):
    poems = Poem.objects.filter(author_id=author_id)
    poem = random.choice(poems)
    return Response({"title": poem.title, "text": poem.text})


@api_view(["GET"])
def random_poem_by_theme(request, theme_id):
    poems = Poem.objects.filter(theme_id=theme_id)
    poem = random.choice(poems)
    return Response({"title": poem.title, "text": poem.text})



@api_view(["GET"])
def poems_by_author(request, author_id):
    poems = Poem.objects.filter(author_id=author_id)
    return Response([p.title for p in poems])


@api_view(["GET"])
def authors_list(request):
    authors = Author.objects.all()
    return Response([a.name for a in authors])


@api_view(["GET"])
def themes_list(request):
    themes = Theme.objects.all()
    return Response([t.name for t in themes])


@api_view(["GET"])
def poems_by_theme(request, theme_id):
    poems = Poem.objects.filter(theme_id=theme_id)
    return Response([p.title for p in poems])
