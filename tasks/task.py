from django.urls import path
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    # Mapea a {{url}}/tasks/
    path('', TaskListCreateView.as_view(), name='task-list-create'),
    # Mapea a {{url}}/tasks/{id}/
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]