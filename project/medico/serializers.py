from rest_framework import serializers

from .models import Especialidad, Medico, Review


class EspecialidadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Especialidad
        fields = '__all__'


class MedicoSerializer(serializers.ModelSerializer):
    especialidad = serializers.ReadOnlyField(source='especialidad.especialidad')

    class Meta:
        model = Medico
        fields = '__all__'