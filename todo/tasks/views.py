from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.template import loader
from django.urls import reverse

from .models import Task
from django.contrib.auth.models import User
import datetime

# get tasks and display them
def index(request):
    if request.user.is_authenticated:
        latest_tasks = Task.objects.order_by('-updated_date')
        username = request.user.get_username()
        context = {
            'latest_task_list' : latest_tasks,
            'username' : username
            }
        return render(request, 'todo/index.html', context)
    else:
        return render(request, 'account/login.html')

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
    new_title = request.POST['task_title']
    new_description = request.POST['task_description']
    user = request.user
    if new_description == "":
        new_description = None
    if request.method == 'POST':
        if new_title == "":
            return redirect('/')
        task_obj = Task(author=user, task_title=new_title, task_description=new_description)
        task_obj.save()
        return redirect('/')
    return render(request, 'todo/index.html')

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    new_title = request.POST['task_title']
    new_description = request.POST['task_description']
    if new_description == "":
        new_description = None
    if request.method == 'POST':
        if new_title == "":
            return redirect('/')
        task.task_title = new_title
        task.task_description = new_description
        task.updated_date = datetime.datetime.now()
        task.save()
        return redirect('/')
    return render(request, 'todo/index.html')