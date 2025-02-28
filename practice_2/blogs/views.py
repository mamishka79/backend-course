from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogCreationForm

def get_students_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        form = BlogCreationForm()
        return render(request, 'index2.html', {'blogs': blogs, 'form': form})
    elif request.method == 'POST':
        form = BlogCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blogs/')
        else:
            blogs = Blog.objects.all()
            return render(request, 'index2.html', {'blogs': blogs, 'form': form})


def get_student(request, pk):
    w = Blog.objects.get(id=pk)
    return render(request, 'product-details.html', {'blog': w})

def delete_todo(request, pk):
    try:
        todo = Blog.objects.get(id=pk)
        todo.delete()
        return redirect('/blogs/')
    except Blog.DoesNotExist as e:
        blogs = Blog.objects.all()
        form = BlogCreationForm()
        return render(request, 'index2.html', {'blogs': blogs, 'form': form, 'error': 'Blog does not exist'})
