from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse

from .models import Task
import datetime

# get tasks and display them
def index(request):
    latest_tasks = Task.objects.order_by('-updated_date')
    context = {'latest_task_list' : latest_tasks}
    return render(request, 'todo/index.html', context)

# show specific task
def detail(request, task_id):
    pass

# delete specific task
def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request, 'todo/index.html', {'task': task})

# mark task as complete
def toggle_complete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.completed = not task.completed
        task.updated_date = datetime.datetime.now()
        task.save()
        return redirect('/')
    return render(request, 'todo/index.html', {'task': task})

# add new task, probably will need more parameters
def add_task(request):
    if request.method == 'POST':
        task_obj = Task(task_title=request.POST['task_title'])
        task_obj.save()
        return redirect('/')
    return render(request, 'todo/index.html')