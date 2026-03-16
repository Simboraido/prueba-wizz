from django.db import models
from django.conf import settings

class Task(models.Model):
    # Definimos los estados posibles usando TextChoices para mayor orden
    class StatusChoices(models.TextChoices):
        PENDING = 'PENDING', 'Pendiente'
        IN_PROGRESS = 'IN_PROGRESS', 'En progreso'
        COMPLETED = 'COMPLETED', 'Completada'

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )
    # Relación: Una tarea pertenece a un usuario (el que la crea)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    # Campos de auditoría automáticos
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
