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

def userdetails(request):
    sum = 0
    data = {}
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            sum= n1+n2
            data = {
                'n1' : n1,
                'n2' : n2,
                'output' : sum
            }
    except:
        pass
    return render(request, "userdetails.html", data)

