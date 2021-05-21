from .serializers import CollectionListSerializer, CollectionSerializer, MoviesListSerializer
from .models import Collection, Movie

from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model

# Create your views here.
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
class CollectionView(APIView):

    def get(self, request, collection_id):
        collection = get_object_or_404(Collection, id=collection_id)
        Serializer = CollectionSerializer(collection)
        return Response(Serializer.data)

    def delete(self, request, collection_id):
        collection = get_object_or_404(Collection, id=collection_id)
        collection.delete()
        return Response({'id' : collection_id }, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, collection_id):
        collection = get_object_or_404(Collection, id=collection_id)
        if not request.user.collection_set.filter(pk=collection_id.pk).exists():
            return Response({'detail': '권한없다'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CollectionSerializer(collection, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



class CollectionListView(APIView):

    def get(self, request, user_id):
        person = get_object_or_404(get_user_model(), pk=user_id)
        serializer = CollectionListSerializer(person.collection_set, many=True)
        return Response(serializer.data)

    @authentication_classes([JSONWebTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def post(self, request):
        movies = request.POST['movies']
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            serializer.movies.add(*movies)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
class MovieListView(APIView):

    def get(self, request):
        movies = Movie.objects.order_by('popularity')
        serializer = MoviesListSerializer(movies, many=True)
        return Response(serializer.data)

    # def post(self, request):
    #     movies = request.POST['movies']
    #     serializer = CollectionSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(user=request.user)
    #         serializer.movies.add(*movies)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
