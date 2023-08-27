from django.shortcuts import render

# Create your views here.

def task_list(request):
    incomplete_tasks = ["Task 1", "Task 2"]  # Replace with your data
    completed_tasks = ["Task 3", "Task 4"]    # Replace with your data
    return render(request, 'taskmanager.html', {'incomplete_tasks': incomplete_tasks, 'completed_tasks': completed_tasks})