from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def blogs(request):
    return HttpResponse("My 1st bolgs data!!")
def home(request):
    return HttpResponse("<h1>Welcome to My Website!</h1><p>This is my Home Page.</p>")