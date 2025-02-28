from django.urls import path
from .views import get_students_list, get_student, delete_todo, get_index_page, edit_todo, get_todo_lists_list, edit_todo_list, delete_todo_list, get_todo_list_todos

urlpatterns = [
    path('', get_index_page, name='index_page'),

    path('todo-lists/', get_todo_lists_list, name='todo_lists_list_page'), # GET List, POST
    path('todo-lists/<int:pk>/edit', edit_todo_list, name='edit_todo_list'),
    path('todo-lists/<int:pk>/delete', delete_todo_list, name='delete_todo_list'),
    path('todo-lists/<int:pk>/todos', get_todo_list_todos, name='todo_list_todo_list'),

    path('todos/', get_students_list, name='todos_list_page'),
    path('todos/<int:pk>/', get_student, name='todo_details_page'),
    path('todos/<int:pk>/edit', edit_todo, name='edit_todo'),
    path('todos/<int:pk>/delete/', delete_todo, name='delete_todo')
]
