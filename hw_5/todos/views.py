from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo, TodoList
from .forms import StudentCreationForm, TodoListForm, EditTodoForm

@login_required
def get_index_page(request):
    todos = Todo.objects.filter(owner=request.user)
    form = StudentCreationForm()
    return render(request, 'index2.html', {'todos': todos, 'form': form})

@login_required
def get_todo_lists_list(request):
    if request.method == 'GET':
        todo_lists = TodoList.objects.filter(owner=request.user)
        form = TodoListForm()
        return render(request, 'todo_lists.html', {'form': form, 'todo_lists': todo_lists})
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.owner = request.user
            todo_list.save()
            return redirect(to='todo_lists_list_page')
        else:
            todo_lists = TodoList.objects.filter(owner=request.user)
            return render(request, 'todo_lists.html', {'form': form, 'todo_lists': todo_lists, 'error': 'SOMETHING WENT WRONG'})

@login_required
def edit_todo_list(request, pk):
    todo_list = get_object_or_404(TodoList, id=pk, owner=request.user)
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

@login_required
def delete_todo_list(request, pk):
    todo_list = get_object_or_404(TodoList, id=pk, owner=request.user)
    todo_list.delete()
    return redirect(to='todo_lists_list_page')

@login_required
def get_todo_list_todos(request, pk):
    print('okokokok')
    if request.method == 'GET':
        todo_list = get_object_or_404(TodoList, id=pk, owner=request.user)
        print(todo_list)
        todos = Todo.objects.filter(todo_list_id=todo_list.id, owner=request.user)
        form = StudentCreationForm()
        return render(request, 'todo_list-todos.html', {'todo_list': todo_list, 'todos': todos, 'form': form})
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        todo_list = get_object_or_404(TodoList, id=pk, owner=request.user)
        if form.is_valid():
            status_value = request.POST.get('status') == 'on'
            title = form.data.get('title')
            description = form.data.get('description')
            due_date = form.cleaned_data.get('due_date')
            status = status_value
            todo_list_id = todo_list.id
            new_todo = Todo(title=title, description=description, due_date=due_date, status=status, todo_list_id=todo_list_id, owner=request.user)
            new_todo.save()
            return redirect('todo_list_todo_list', pk=todo_list.id)
        else:
            return render(request, 'todo_list-todos.html', {'todo_list': todo_list, 'todos': todos, 'form': form, 'error': 'ERROR!'})

@login_required
def get_students_list(request):
    if request.method == 'GET':
        todos = Todo.objects.filter(owner=request.user)
        form = StudentCreationForm()
        return render(request, 'index2.html', {'todos': todos, 'form': form})
    else:
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            title = form.data.get('title')
            description = form.data.get('description')
            due_date = form.data.get('due_date')
            status = request.POST.get('status') == 'on'
            new_todo = Todo(title=title, description=description, due_date=due_date, status=status, owner=request.user)
            new_todo.save()
            return redirect(to='index_page')
        else:
            todos = Todo.objects.all()
            return render(request, 'index2.html', {'todos': todos, 'form': form})

@login_required
def get_student(request, pk):
    w = get_object_or_404(Todo, id=pk, owner=request.user)
    return render(request, 'product-details.html', {'todo': w})

@login_required
def delete_todo(request, pk):
    try:
        todo = get_object_or_404(Todo, id=pk, owner=request.user)
        todo.delete()
        return redirect('/todos/')
    except Todo.DoesNotExist as e:
        todos = Todo.objects.all()
        form = StudentCreationForm()
        return render(request, 'index2.html', {'todos': todos, 'form': form, 'error': 'Todo does not exist'})

@login_required
def edit_todo(request, pk):
    todo_lists = TodoList.objects.all()
    if request.method == 'GET':
        todo = get_object_or_404(Todo, id=pk, owner=request.user)
        todo_list_id = todo.todo_list.id
        form = EditTodoForm(data={'title': todo.title, 'description': todo.description, 'due_date': todo.due_date, 'status': todo.status, 'todo_list_id': todo_list_id})
        return render(request, 'edit-todo.html', {'form': form, 'todo': todo, 'todo_lists': todo_lists})
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=pk, owner=request.user)
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