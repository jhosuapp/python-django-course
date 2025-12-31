from django.shortcuts import render

# Create your views here.

def indexTodo(request):
    todos = [
        {
            "title": "Título de mi primera TODO",
            "description": "descripción de mi TODO",
            "is_checked": False,
        },
        {
            "title": "Título de mi segunda TODO",
            "description": "descripción de mi TODO",
            "is_checked": True,
        },
    ]
    response = { 'todos': todos }
    return render(request, 'todo/index.html', response)