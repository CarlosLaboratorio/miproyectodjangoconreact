from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','title','description','done')
        # fields = '__all__' Esta linea si la cambias por la anterior te permite convertir a todos los campos solo con esta linea
        
        
        