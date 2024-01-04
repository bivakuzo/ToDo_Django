
from django.shortcuts import render

from todo.models import Task


def home(requests):
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')   # With - means descending order, WithOut - means ascending order
    
    completed_tasks = Task.objects.filter(is_completed = True)

    context = {
        'tasks' : tasks,
        'completed_tasks' : completed_tasks,
    }
    
    return render(requests, 'home.html', context)