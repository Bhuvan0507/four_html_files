from django.shortcuts import render

# Create your views here.

def developers(request):
    return render(request,'developers.html')

def frinds(request):
    return render(request,"frinds.html")

def hackers(request):
    return render(request,"hackers.html")

def heroes(request):
    return render(request,"heroes.html")
