from rest_framework import serializers

from .models import Especialidad, Medico, Review

class MedicoSerializer(serializers.ModelSerializer):

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