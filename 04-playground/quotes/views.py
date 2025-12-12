from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import redirect


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

def days_week(request, day):
    try:
        return HttpResponse(days_of_week[day])
    except: 
        return HttpResponseRedirect('ese día no existe')    
    

def days_week_with_number(request, day):
    try:
        days = list(days_of_week.keys())
        if day-1 > len(days):
            # return HttpResponseRedirect('day-quote')      
            return redirect('day-quote', day='monday')
        else:
            return HttpResponse(days_of_week[days[day-1]])        
    except:
        return HttpResponseBadRequest('Ha ocurrido un error')      