from django.urls import path

from .views import *


app_name = 'to_do'
urlpatterns = [
    path('nuevo/', create_task, name='create_task'),
    path('<int:task_id>/actualizar/', update_task, name='update_task'),
    path('<int:task_id>/eliminar/', delete_task, name='delete_task'),
    path('', list_tasks, name='list_tasks'),
]
