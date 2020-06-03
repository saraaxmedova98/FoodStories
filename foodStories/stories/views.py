from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("Home")

def about(request):
    return HttpResponse("About")

def stories(request):
    return HttpResponse("Stories")

def recipes(request):
    return HttpResponse("Recipes")

def contact(request):
    return HttpResponse("Contact")