from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk:int):
    task = get_object_or_404(Task, pk=pk)   # Getting the task
    task.is_completed = True    # Modifying to completed
    task.save() # Saving the task
    return redirect('home')

def mark_as_undone(request, pk:int):
    task = get_object_or_404(Task, pk=pk)   # Getting the task
    task.is_completed = False    # Modifying to incomplete
    task.save() # Saving the task
    return redirect('home')

def edit_task(request, pk:int):
    get_task = get_object_or_404(Task, pk=pk)   # Getting the task
    if request.method == 'POST':    # Checking if the request is POST
        new_task = request.POST['task'] # Getting the new task
        get_task.task = new_task    # Assigning it to the DB
        get_task.save() # Saving
        return redirect('home') # Redirecting to home page
    else:   # if request is GET
        context = {
            'get_task' : get_task,
        }
        return render(request, 'edit_task.html', context)

def delete_task(request, pk:int):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')