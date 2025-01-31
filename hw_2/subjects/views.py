from django.shortcuts import render
from .models import Course


def get_subjects_list(request):
    subjects = Course.objects.all()
    return render(request, 'subjects.html',    {'subjects': subjects})


def get_subject(request, pk):
    subject = Course.objects.get(id=pk)
    return render(request, 'subject-details.html', {'subject': subject})