from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponseBadRequest, Http404
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
    list_days = []
    days = list(days_of_week.keys())
    
    for day in days:
        day_path = reverse('day-quote',  kwargs={'day': day}) 
        list_days.append({
            "url": day_path,
            "day": day
        })
    response = {
        "days": list_days,
        "name": "Jhosua"    
    }
    
    return render(request, "quotes/quotes.html", response)


def days_week(request, day):
    try:
        response = {
            "day": days_of_week[day],
            "name": "Jhosua"
        }
        
        return render(request, "quotes/day.html", response)
    except Exception: 
        # redirect_path = reverse('quotes')      
        # return Http404(request, '404.html')
        raise Http404()

def days_week_with_number(request, day):
    try:
        days = list(days_of_week.keys())
        if day-1 > len(days):
            # return HttpResponseRedirect('day-quote')
            # redirect_path = reverse('day-quote',  kwargs={'day': 'monday'})      
            return redirect('quote')
        else:
            return redirect('day-quote', day=days_of_week[days[day-1]])        
    except Exception as error:
        print(error)
        return HttpResponseBadRequest('Ha ocurrido un error')      