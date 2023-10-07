from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import filters
from rest_framework.response import Response

from .models import Medico, Review
from .serializers import MedicoSerializer, ReviewSerializer


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def login(request):
    return render(request, 'login.html', {})


def docprofile(request):
    medicos = Medico.objects.all()
    return render(request, 'docprofile.html', {'medicos':  medicos})


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
    aa, bb = queryset.query.sql_with_params()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['rating']
    search_fields = ['^especialidad__especialidad', '^name', '^surname']


class Search_(ListAPIView):
    serializer_class = MedicoSerializer

    def get_queryset(self):
        print(self.request.GET['search'])
        search = self.request.GET['search']
        qs = Medico.objects.filter(
            especialidad__especialidad__icontains=search)
        return qs


class DocReviewList(ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self, *args, **kwargs):
        medico_id = self.kwargs['medico_id']

        if 'score' in self.kwargs:
            score = self.kwargs['score']
            return Review.objects.filter(medico=medico_id, score=score)
        return Review.objects.filter(medico=medico_id)
