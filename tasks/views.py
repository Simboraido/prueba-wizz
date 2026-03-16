from django.shortcuts import render

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

# Vista para GET (Listar) y POST (Crear) en {{url}}/tasks/
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated] # Exige que el usuario envíe su token JWT
    
    # Configuración para ganar los puntos extra de filtros y ordenamiento
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description'] # Permite buscar texto en estos campos
    ordering_fields = ['created_at', 'status'] # Permite ordenar por fecha o estado
    ordering = ['-created_at'] # Por defecto, muestra las más nuevas primero

    def get_queryset(self):
        queryset = Task.objects.all()
        # Filtro manual exacto por estado (ej: /tasks/?status=PENDING)
        status_param = self.request.query_params.get('status', None)
        if status_param is not None:
            queryset = queryset.filter(status=status_param)
        return queryset

    def perform_create(self, serializer):
        # Asigna automáticamente al usuario autenticado como el creador de la tarea
        serializer.save(created_by=self.request.user)


# Vista para GET (Detalle), PATCH (Actualizar) y DELETE (Eliminar) en {{url}}/tasks/{id}/
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated] # Exige token JWT
    # RetrieveUpdateDestroyAPIView ya soporta PATCH y DELETE por defecto