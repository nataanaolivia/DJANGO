from django.shortcuts import render
from django. http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Welcome to homepage")

def about(request):
    return HttpResponse("Welcome to about page")

def services(request):
    return HttpResponse("Welcome to my  services")
