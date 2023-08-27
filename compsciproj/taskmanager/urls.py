from django.urls import path
from . import views

urlpatterns = [
    path('taskmanager/', views.task_list, name='task_list'),
]
