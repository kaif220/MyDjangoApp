from django.shortcuts import render

from django.http import HttpResponse

def rendersomething(req):
    return render(req,"index.html")

def Aboutsomething(req):
    return HttpResponse("my Second application")