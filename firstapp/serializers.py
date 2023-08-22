from rest_framework import serializers

from .models import Especialidad, Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = (
            'id', 
            'name', 
            'surname', 
            'especialidad', 
            'date_added', 
            'rating'
        )