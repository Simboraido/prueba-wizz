from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        # Hacemos que el creador sea de solo lectura para asignarlo por detrás
        read_only_fields = ('created_by', 'created_at', 'updated_at')