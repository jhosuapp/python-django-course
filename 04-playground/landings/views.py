from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    response = { "name": "Jhosua" }
    return render(request, "landings/landing.html", response)