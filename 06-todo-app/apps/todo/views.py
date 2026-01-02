from django.shortcuts import render, get_object_or_404
from .models import Todo
from django.db.models import Q

# Create your views here.

def indexTodo(request):
    query = request.GET.get('q', '')

    todos = Todo.objects.all()

    if query:
        todos = todos.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    response = {
        'todos': todos,
    }
    return render(request, 'todo/index.html', response)

def detailTodo(request, id):
    todo = get_object_or_404(Todo, id=id)
    response = {'todo': todo}
    
    return render(request, 'todo/detail.html', response)