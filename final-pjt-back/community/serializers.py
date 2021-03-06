from rest_framework import serializers
from .models import Review, Comment
from movies.serializers import MoviesSerializer


class ReviewListSerializer(serializers.ModelSerializer):
    movie = MoviesSerializer()
    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review','user',)


class ReviewSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie','user','like_users')