from django.urls import path
from .views import get_students_list, get_student

urlpatterns = [
    path('', get_students_list),
    path('<int:pk>/', get_student)
]