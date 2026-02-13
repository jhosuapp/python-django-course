from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from django.db.models import Q
from .forms import TodoForm

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


def createTodo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')  # nombre de tu url principal
    else:
        form = TodoForm()

    return render(request, 'todo/create.html', {
        'form': form
    })