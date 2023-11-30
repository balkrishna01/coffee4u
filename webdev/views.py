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

def userform(request):
    sum = 0
    try:
        n1 = int(request.GET['num1'])
        n2 = int(request.GET['num2'])
        sum= n1+n2
    except:
        pass
    return render(request, "userform.html", {'output':sum})
