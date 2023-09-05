from rest_framework import serializers

from .models import Especialidad, Medico, Review


class EspecialidadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Especialidad
        fields = '__all__'


class MedicoSerializer(serializers.ModelSerializer):
    especialidad = EspecialidadSerializer()

    class Meta:
        model = Medico
        fields = (
            'id', 
            'name', 
            'surname', 
            'especialidad', 
            'date_added', 
            'average_rating'
        )