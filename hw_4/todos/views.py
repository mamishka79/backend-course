from django.shortcuts import render, redirect
from .models import Todo, TodoList
from .forms import StudentCreationForm, TodoListForm, EditTodoForm

def get_index_page(request):
    todos = TodoList.objects.all()
    form = StudentCreationForm()
    return render(request, 'index2.html', {'todos': todos, 'form': form})

def get_todo_lists_list(request):
    if request.method == 'GET':
        todo_lists = TodoList.objects.all()
        form = TodoListForm()
        return render(request, 'todo_lists.html', {'form': form, 'todo_lists': todo_lists})
    if request.method == 'POST':
        todo_lists = TodoList.objects.all()
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = TodoList(title=form.data.get('title'), description=form.data.get('description'))
            todo_list.save()
            return redirect(to='todo_lists_list_page')
        else:
            return render(request, 'todo_lists.html', {'form': form, 'todo_lists': todo_lists, 'error': 'SOMETHING WENT WRONG'})


def edit_todo_list(request, pk):
    todo_list = TodoList.objects.get(id=pk)
    if request.method == 'GET':
        form = TodoListForm(initial={'title': todo_list.title, 'description': todo_list.description})
        return render(request, 'edit-todo_list.html', {'form': form, 'todo_list': todo_list})
    elif request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list.title = form.cleaned_data.get('title')
            todo_list.description = form.cleaned_data.get('description')
            todo_list.save()
            return redirect('todo_lists_list_page')
        else:
            return render(request, 'edit-todo_list.html',
                          {'form': form, 'todo_list': todo_list, 'error': 'SOMETHING WENT WRONG'})


def delete_todo_list(request, pk):
    todo_list = TodoList.objects.get(id=pk)
    todo_list.delete()
    return redirect(to='todo_lists_list_page')

def get_todo_list_todos(request, pk):
    print('okokokok')
    if request.method == 'GET':
        todo_list = TodoList.objects.get(id=pk)
        print(todo_list)
        todos = Todo.objects.filter(todo_list_id=todo_list.id)
        form = StudentCreationForm()
        return render(request, 'todo_list-todos.html', {'todo_list': todo_list, 'todos': todos, 'form': form})
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        todo_list = TodoList.objects.get(id=pk)
        if form.is_valid():
            status_value = request.POST.get('status') == 'on'
            title = form.data.get('title')
            description = form.data.get('description')
            due_date = form.cleaned_data.get('due_date')
            status = status_value
            todo_list_id = todo_list.id
            new_todo = Todo(title=title, description=description, due_date=due_date, status=status, todo_list_id=todo_list_id)
            new_todo.save()
            return redirect('todo_list_todo_list', pk=todo_list.id)
        else:
            return render(request, 'todo_list-todos.html', {'todo_list': todo_list, 'todos': todos, 'form': form, 'error': 'ERROR!'})

def get_students_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        form = StudentCreationForm()
        return render(request, 'index2.html', {'todos': todos, 'form': form})
    else:
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            title = form.data.get('title')
            description = form.data.get('description')
            due_date = form.data.get('due_date')
            status = request.POST.get('status') == 'on'
            new_todo = Todo(title=title, description=description, due_date=due_date, status=status)
            new_todo.save()
            return redirect(to='index_page')
        else:
            todos = Todo.objects.all()
            return render(request, 'index2.html', {'todos': todos, 'form': form})

def get_student(request, pk):
    w = Todo.objects.get(id=pk)
    return render(request, 'product-details.html', {'todo': w})

def delete_todo(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return redirect('/todos/')
    except Todo.DoesNotExist as e:
        todos = Todo.objects.all()
        form = StudentCreationForm()
        return render(request, 'index2.html', {'todos': todos, 'form': form, 'error': 'Todo does not exist'})

def edit_todo(request, pk):
    todo_lists = TodoList.objects.all()
    if request.method == 'GET':
        todo = Todo.objects.get(id=pk)
        todo_list_id = todo.todo_list.id
        form = EditTodoForm(data={'title': todo.title, 'description': todo.description, 'due_date': todo.due_date, 'status': todo.status, 'todo_list_id': todo_list_id})
        return render(request, 'edit-todo.html', {'form': form, 'todo': todo, 'todo_lists': todo_lists})
    if request.method == 'POST':
        todo = Todo.objects.get(id=pk)
        form = EditTodoForm(request.POST)
        if form.is_valid():
            status_value = request.POST.get('status') == 'on'
            todo.title = form.data.get('title')
            todo.description = form.data.get('description')
            todo.due_date = form.data.get('due_date')
            todo.status = status_value
            todo.todo_list_id = form.data.get('todo_list_id')
            todo.save()
            return redirect(to='todo_list_todo_list', pk=form.data.get('todo_list_id'))
        else:
            return render(request, 'edit-todo.html', {'form': form, 'todo': todo, 'error': 'Something went wrong'})