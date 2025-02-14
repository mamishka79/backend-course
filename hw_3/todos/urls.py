from django.urls import path
from .views import get_students_list, get_student, delete_todo

urlpatterns = [
    path('', get_students_list, name='todos_list'),
    path('<int:pk>/', get_student, name='todo_details'),
    path('<int:pk>/delete/', delete_todo)
]
