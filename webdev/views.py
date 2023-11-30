from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    # data={
    #     'title':'Home Page',
    #     'bdata': 'Welcome to Home Page!!',
    #     'clist': ['PHP', 'Java', 'Django'],
    #     'numbers': [10,20,30,40,50,60,70,80],
    #     'student_details': [
    #         {'name':'Pradip','phone':'9845645654'},
    #         {'name':'Peter','phone':'984564565465'}
    #     ]
    # }
    return render(request, "index.html")

def aboutUS(request):
    return HttpResponse("Welcome to about Us!")

def course(request):
    return HttpResponse("Welcome to course!!")

def courseDetails(request, courseid):
    return HttpResponse(f"Welcome to courseid : {courseid}")