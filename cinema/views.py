from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from django.shortcuts import get_object_or_404

from cinema.models import Actor, CinemaHall, Genre, Movie
from cinema.serializers import (
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    MovieSerializer
)


class GenreList(APIView):
    def get(self, rquset):
        genre_list = Genre.objects.all()
        serializer = GenreSerializer(genre_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Genre, pk=pk)

    def get(self, reuest, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, response, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=response.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, response, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=response.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, response, pk):
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(
    GenericViewSet,
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
