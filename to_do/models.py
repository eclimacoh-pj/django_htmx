from django.db import models


class Tasks(models.Model):
    HIGH = 'H'
    MIDDLE = 'M'
    LOW = 'L'

    PRIORITY_TASKS_CHOICES = [
        (HIGH, 'ALTO'),
        (MIDDLE, 'MEDIO'),
        (LOW, 'BAJO'),
    ]

    name = models.CharField('Tarea', max_length=500, unique=True, blank=False, null=False)
    priority = models.CharField('Prioridad', max_length=5, choices=PRIORITY_TASKS_CHOICES, default=LOW)
    status = models.BooleanField('Estado', choices=((True, 'COMPLETADO'), (False, 'Pending')), default=False)
    enable = models.BooleanField('Activo', choices=((True, 'Habilitado'), (False, 'Inhabilitado')), default=True)

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        return self.name
