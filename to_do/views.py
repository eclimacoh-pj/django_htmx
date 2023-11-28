import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .models import *
from .forms import *


def create_task(request):
    # template = 'to_do/create_task.html'


    # context = {
    #     'form': form
    # }
    context = {}
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        context['form'] = form
        if form.is_valid():
            task = form.save()
            # Código para usarlo con HTMX.
            # task = Tasks.objects.create(
            #     name = form.cleaned_data['name'],
            #     priority = form.cleaned_data['priority'],
            # )

                # status = form.cleaned_data['status']
                # enable = form.cleaned_data['enable']

            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        'tasksListChanged': None,
                        'showMessage': f'{task.name} creado con éxito.'
                    })
                }
            )
        else:
            return render(request, 'to_do/create_task.html', context)
    else:
        form = CreateTaskForm()
        context['form'] = form
    return render(request, 'to_do/create_task.html', context)

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
    template = 'to_do/create_task.html'
    context = {}
    form = CreateTaskForm(instance=task)
    context['form'] = form
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=task)
        context['form'] = form
        if form.is_valid():
            task = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        'tasksListChanged': None,
                        'showMessage': f'{task.name} actualizado con éxito.'
                    })
                }
            )
        else:
            return render(request, template, context)
            # messages.success(
            #     request,
            #     f'Tarea {task.name} actualizada con éxito.'
            # )
            # return redirect('to_do:list_tasks')
    # template = 'to_do/create_task.html'
    # context = {
    #     'form': form,
    # }
    return render(request, template, context)


@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                'tasksListChanged': None,
                'showMessage': f'{task.name} eliminado con éxito.'
            })
        }
    )
    # if request.method == 'POST':
    #     task.enable = False
    #     task.save()
    #     messages.success(
    #         request,
    #         f'Tarea {task.name} eliminada con éxito.'
    #     )
    #     return redirect('to_do:list_tasks')
    # template = 'to_do/delete_task.html'
    # context = {
    #     'task': task
    # }
    # return render(request, template, context)


def delete_task_confirmation(request, task_id):
    task = get_object_or_404(Tasks, pk=task_id)
    template = 'to_do/delete_task.html'
    context = {'task': task}
    return render(request, template, context)


def list_tasks(request):
    tasks = Tasks.objects.all()
    # template = 'to_do/list_tasks.html'
    template = 'to_do/list_tasks.html'
    context = {
        'tasks': tasks,
    }
    return render(request, template, context)


def tasks(request):
    tasks = Tasks.objects.all()
    # template = 'to_do/list_tasks.html'
    template = 'to_do/tasks.html'
    context = {
        'tasks': tasks,
    }
    return render(request, template, context)
