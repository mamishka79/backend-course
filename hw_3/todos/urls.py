from django.urls import path
from .views import get_todos, get_todo, create_todo, delete_todo

urlpatterns = [
    path('', get_todos, name='todos_list'),
    path('<int:id>/', get_todo, name='todo_detail'),
    path('create/', create_todo, name='todo_create'),
    path('<int:id>/delete/', delete_todo, name='todo_delete'),
]
