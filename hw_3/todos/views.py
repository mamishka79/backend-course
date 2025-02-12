from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

def get_todos(request):
    todos = Todo.objects.all()
    return render(request, 'todos/list.html', {'todos': todos})

def get_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todos/detail.html', {'todo': todo})

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos_list')
    else:
        form = TodoForm()
    return render(request, 'todos/create.html', {'form': form})

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todos_list')
