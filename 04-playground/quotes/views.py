from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.

days_of_week = {
    "monday": "monday",
    "tuesday": "tuesday",
    "wednesday": "wednesday",
    "thursday": "thursday",
    "friday": "friday",
    "saturday": "saturday",
    "sunday": "sunday"
}

def index(request):
    list_items = ''
    days = list(days_of_week.keys())
    
    for day in days:
        day_path = reverse('day-quote',  kwargs={'day': day}) 
        list_items += f'<li><a href="{day_path}">{ day }</a></li>'
    
    ul = f'<ul>{list_items}</ul>'
    
    return HttpResponse(ul)

def days_week(request, day):
    try:
        return HttpResponse(days_of_week[day])
    except Exception: 
        return HttpResponseNotFound('ese día no existe')    
    

def days_week_with_number(request, day):
    try:
        days = list(days_of_week.keys())
        if day-1 > len(days):
            # return HttpResponseRedirect('day-quote')
            # redirect_path = reverse('day-quote',  kwargs={'day': 'monday'})      
            return redirect('day-quote', day='monday')
        else:
            return HttpResponse(days_of_week[days[day-1]])        
    except:
        return HttpResponseBadRequest('Ha ocurrido un error')      