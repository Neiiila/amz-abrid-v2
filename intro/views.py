from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render

# Create your views here.
def index (request) : 
    return render(request, 'intro/index.html')

def voyage(request) : 
    return render(request, 'voyages/voyage.html')