from django.urls import path
from .views import get_students_list, get_student, delete_todo, get_index_page

urlpatterns = [
    path('', get_index_page, name='index_page'),
    path('todos/', get_students_list, name='todos_list_page'),
    path('todos/<int:pk>/', get_student, name='todo_details_page'),
    path('todos/<int:pk>/delete/', delete_todo, name='delete_todo')
]
