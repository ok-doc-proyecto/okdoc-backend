from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import viewsets, mixins, filters
from rest_framework.response import Response
from .models import Medico, Review
from .serializers import MedicoSerializer, ReviewSerializer
from django.http import JsonResponse
from asgiref.sync import async_to_sync

import asyncio
from django.utils.decorators import classonlymethod


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

    @classmethod
    def x_get_queryset(cls, p_medico):
        """ permite obtener el queryset que usa el view  """
        queryset = Review.objects.filter(medico__exact=p_medico)
        return queryset

    @classmethod
    async def asyncProviderDocReviews(*args, **kwargs):
        queryset = DocReviews.x_get_queryset(kwargs["medico_id"])
        data = [review async for review in queryset.values()]
        return data

    def get_queryset(self, *args, **kwargs):
        medico_id = self.kwargs['medico_id']
        queryset = self.x_get_queryset(medico_id)
        return queryset

    def list_orginal(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        w_data = serializer.data
        w_response = Response(w_data)
        return w_response

    def list(self, request, *args, **kwargs):
        w_data = async_to_sync(
            DocReviews.asyncProviderDocReviews)(*args, **kwargs)
        w_response = Response(w_data)
        return w_response

    @classmethod
    async def asyncDocReviews(request, *args, **kwargs):
        data = await DocReviews.asyncProviderDocReviews(*args, **kwargs)
        w_response = JsonResponse(data, safe=False)
 #      w_response = Response(data)
 #      w_response.accepted_media_type = 'text/html'
 #      w_response.accepted_renderer=BrowsableAPIRenderer
 #      w_response.renderer=BrowsableAPIRenderer
 #      w_response.context =

        return w_response
