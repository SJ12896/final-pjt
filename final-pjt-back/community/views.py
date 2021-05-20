from .models import Review, Comment

from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ReviewSerializer,ReviewListSerializer, CommentSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

# Create your views here.
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
class ReviewView(APIView):

    def get(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        Serializer = ReviewSerializer(review)
        return Response(Serializer.data)

    def delete(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        review.delete()
        return Response({'id' : review_id }, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        if not request.user.review_set.filter(pk=review.pk).exists():
            return Response({'detail': '권한없다'}, status=status.HTTP_403_FORBIDDEN)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
class MovieReview(APIView):

    def get(self, request, movie_id):
        movie = get_object_or_404(Review, id=movie_id)
        Serializer = ReviewListSerializer(movie.set_review, many=True)
        return Response(Serializer.data)

    def post(self, request, movie_id):
        movie = get_object_or_404(Review, id=movie_id)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
class CommentView(APIView):

    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return Response({'id' : comment_id }, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if not request.user.comment_set.filter(pk=comment.pk).exists():
            return Response({'detail': '권한없다'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
class ReviewComment(APIView):

    # def get(self, request, movie_id):
    #     movie = get_object_or_404(Review, id=movie_id)
    #     Serializer = ReviewListSerializer(movie.set_review, many=True)
    #     return Response(Serializer.data)

    def post(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        