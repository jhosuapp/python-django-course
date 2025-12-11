from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def days_week(request, day):
    quote_text = None
    if(day == 'monday'):
        quote_text = 'Pienso, luego existo'
    elif(day == 'tuesday'):
        quote_text = 'La vida es un sueño'
    else:
        return HttpResponseNotFound('No hay frase para este día.')
    
    return HttpResponse(quote_text)

def days_week_with_number(request, day):
    arr_days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    text = None
    if(arr_days[day - 1]):
        text = arr_days[day - 1]        
    else:
        return HttpResponseNotFound(f'No existe el día {day}')
        
    return HttpResponse(text)