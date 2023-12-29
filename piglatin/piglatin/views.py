from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def translate(request):
    original = request.GET["originaltext"].lower()

    translated = ''
    for word in original.split():
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            translated += word
            translated += 'ay '
        else:
            translated += word[1:]
            translated += word[0]
            translated += 'ay '
    return render(request, "translated.html", {'original':original, 'translated':translated})

def about(request):
    return render(request, "about.html")
