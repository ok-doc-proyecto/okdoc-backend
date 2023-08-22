from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Medico
from .serializers import MedicoSerializer


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def login(request):
    return render(request, 'login.html', {})

def docprofile(request):
    return render(request, 'docprofile.html', {})

def userprofile(request):
    return render(request, 'userprofile.html', {})

class AllDocsList(APIView):
    def get(self, request, format=None):
        medicos = Medico.objects.all()
        serializer = MedicoSerializer(medicos, many=True)
        return Response(serializer.data)