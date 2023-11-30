from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")

def aboutUS(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
