from rest_framework import serializers

from .models import Especialidad, Prepaga, Medico, Review


class EspecialidadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Especialidad
        fields = '__all__'


class PrepagaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Prepaga
        fields = '__all__'


class MedicoSerializer(serializers.ModelSerializer):
    especialidades = serializers.StringRelatedField(many=True)
    prepagas = serializers.StringRelatedField(many=True)

    class Meta:
        model = Medico
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    medico = serializers.ReadOnlyField(source='medico.last_name')

    class Meta:
        model = Review
        fields = '__all__'