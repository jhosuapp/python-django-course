from django.shortcuts import render

# Create your views here.

def indexTodo(request):
    todos = [
        {
            "id": 1,
            "title": "Título de mi primera TODO",
            "description": "descripción de mi TODO",
            "is_checked": False,
        },
        {
            "id": 2,
            "title": "Título de mi segunda TODO",
            "description": "descripción de mi TODO",
            "is_checked": True,
        },
    ]
    response = { 'todos': todos }
    return render(request, 'todo/index.html', response)

def detailTodo(request, id):
    response = { 
                'id': id,
                'title': 'Titulo de primera TODO',
                'description': 'Descripciond de mi todo',
                'is_checked': False,
            }
    
    return render(request, 'todo/detail.html', response)