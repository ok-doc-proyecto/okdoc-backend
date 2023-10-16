from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import viewsets, mixins, filters
from rest_framework.response import Response

from .models import Medico, Review
from .serializers import MedicoSerializer, ReviewSerializer


# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

def login(request):
    return render(request, 'login.html', {})


def docprofile(request):
    medicos = Medico.objects.all()
    return render(request, 'docprofile.html', {'medicos':  medicos})


def userprofile(request):
    return render(request, 'userprofile.html', {})


class AllDocsList_(APIView):
    def get(self, request, format=None):
        medicos = Medico.objects.all()
        serializer = MedicoSerializer(medicos, many=True)
        return Response(serializer.data)


class AllDocs(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    Endpoint que devuelve una lista de médicos. Por default devuelve todos, 
    se puede hacer search pro especialidad, prepaga, nombre o apellido. 
    Admite ordenarlos por rating ascendente o descendente.
    """
    serializer_class = MedicoSerializer
    queryset = Medico.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['rating']
    search_fields = ['^especialidades__especialidad', '^prepagas__prepaga',
                     '^first_name', '^last_name']


class Search(ListAPIView):
    serializer_class = MedicoSerializer
    queryset = Medico.objects.all()
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
            w_salida = Review.objects.filter(medico=medico_id, score=score)
        else:
            w_salida = Review.objects.filter(medico=medico_id)
        return w_salida


class DocReviews(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    Endpoint que devuelve todos los reviews de un médico, indicado por id.
    Las reviews se pueden ordenar por fecha y filtrar por score.
    """
    serializer_class = ReviewSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['score']
    ordering_fields = ['date_added']
    ordering = ['-date_added']

    def get_queryset(self, *args, **kwargs):
        medico_id = self.kwargs['medico_id']
        queryset = Review.objects.filter(medico=medico_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        w_data = serializer.data
        w_response = Response(serializer.data)

        return w_response
