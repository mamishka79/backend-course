from django.shortcuts import render, redirect
from .models import Todo
from .forms import StudentCreationForm

def get_index_page(request):
    todos = Todo.objects.all()
    form = StudentCreationForm()
    return render(request, 'index2.html', {'todos': todos, 'form': form})

def get_students_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        form = StudentCreationForm()
        return render(request, 'index2.html', {'todos': todos, 'form': form})

    elif request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            status_value = request.POST.get('status') == 'on'  # Преобразуем 'on' в True
            todo = Todo(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                due_date=form.cleaned_data.get('due_date'),
                status=status_value  # Исправленный статус
            )
            todo.save()
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
