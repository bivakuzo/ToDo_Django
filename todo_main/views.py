
from django.shortcuts import render

from todo.models import Task


def home(requests):
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')   # With - means descending order, WithOut - means ascending order
    context = {
        'tasks' : tasks,
    }
    return render(requests, 'home.html', context)