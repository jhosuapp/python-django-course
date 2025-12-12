from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
def home(request):
    today = date.today()
    stack = [
        {
            "id": "python", 
            "name": "Python"
        },
        {
            "id": "node", 
            "name": "Node"
        },
        {
            "id": "javascript", 
            "name": "Javascript"
        },
    ]
    response = { 
                "today": today, 
                "stack": stack,
                "name": "Jhosua", 
                "age": 24,
            }
    return render(request, "landings/landing.html", response)

def stack(request, tool):
    return HttpResponse(f'Tu tecnología es: { tool }')