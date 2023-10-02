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
    return render(request, 'docprofile.html', {'medicos': medicos})

def userprofile(request):
    return render(request, 'userprofile.html', {})

class AllDocsList_(APIView):
    def get(self, request, format=None):
        medicos = Medico.objects.all()
        serializer = MedicoSerializer(medicos, many=True)
        return Response(serializer.data)

class AllDocs(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    HOLA
    """
    serializer_class = MedicoSerializer
    queryset = Medico.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['rating']
    search_fields = ['^especialidades__especialidad', '^prepagas__prepaga', '^first_name', '^last_name']
    
    
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
        qs = Medico.objects.filter(especialidad__especialidad__icontains=search)
        return qs
    
class DocReviewList(ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self, *args, **kwargs):
        medico_id = self.kwargs['medico_id']
        
        if 'score' in self.kwargs:
            score = self.kwargs['score']
            return Review.objects.filter(medico=medico_id, score=score)
        return Review.objects.filter(medico=medico_id)

class DocReviews(viewsets.ReadOnlyModelViewSet):
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

        return Response(serializer.data)