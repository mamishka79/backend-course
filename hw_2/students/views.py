from django.shortcuts import render
from .models import Student


def get_students_list(request):
    students = Student.objects.all()
    return render(request, 'index.html',    {'students': students})


def get_student(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'student-details.html', {'student': student})