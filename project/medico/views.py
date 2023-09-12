from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import filters
from rest_framework.response import Response

from .models import Medico
from .serializers import MedicoSerializer


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def login(request):
    return render(request, 'login.html', {})

def docprofile(request):
    medicos = Medico.objects.all()
    return render(request, 'docprofile.html', {'medicos': medicos})

def userprofile(request):
    return render(request, 'userprofile.html', {})

class AllDocsList(APIView):
    def get(self, request, format=None):
        medicos = Medico.objects.all()
        serializer = MedicoSerializer(medicos, many=True)
        return Response(serializer.data)
    
class Search(ListAPIView):
    serializer_class = MedicoSerializer
    queryset = Medico.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['rating']
    search_fields = ['^especialidad__especialidad', '^name', '^surname']