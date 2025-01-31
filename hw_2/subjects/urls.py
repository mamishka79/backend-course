from django.urls import path
from .views import get_subjects_list, get_subject

urlpatterns = [
    path('', get_subjects_list),
    path('<int:pk>/', get_subject)
]