import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse

from .models import *
from .forms import *


def create_task(request):
    template = 'to_do/create_task.html'

    form = CreateTaskForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save()
    # Código para usarlo con HTMX.
            return HttpResponse(
                status=200,
                headers={
                    'HX-Trigger': json.dumps({
                        'tasksListChanged': None,
                        'showMessage': f'{task.name} creado con éxito.'
                    })
                }
            )
        else:
            return render(request, template, context)
    return render(request, template, context)

    # Código tradicional para este tipo de vistas.
    #         messages.success(
    #             request,
    #             f'Tarea {task.name} creada con éxito.'
    #         )
    #         return redirect('to_do:list_tasks')
    # template = 'to_do/create_task.html'
    # context = {
    #     'form': form,
    # }
    # return render(request, template, context)

def update_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    form = CreateTaskForm(instance=task)
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            messages.success(
                request,
                f'Tarea {task.name} actualizada con éxito.'
            )
            return redirect('to_do:list_tasks')
    template = 'to_do/create_task.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == 'POST':
        task.enable = False
        task.save()
        messages.success(
            request,
            f'Tarea {task.name} eliminada con éxito.'
        )
        return redirect('to_do:list_tasks')
    template = 'to_do/delete_task.html'
    context = {
        'task': task
    }
    return render(request, template, context)


def list_tasks(request):
    tasks = Tasks.objects.all()
    template = 'to_do/list_tasks.html'
    context = {
        'tasks': tasks,
    }
    return render(request, template, context)
