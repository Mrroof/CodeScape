from django.shortcuts import render, redirect
from django.urls import include
from .models import Task
# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
    return redirect('task_list')