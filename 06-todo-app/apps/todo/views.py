from django.shortcuts import render

# Create your views here.

def indexTodo(request):
    response = { 'test': 'test' }
    return render(request, 'todo/index.html', response)