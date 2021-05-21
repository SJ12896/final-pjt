from rest_framework import serializers
from .models import Collection, Movie


class CollectionListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Collection
        fields = ('title', 'info',)


class CollectionSerializer(serializers.ModelSerializer):
    movie_count = serializers.IntegerField(source='movie.count', read_only=True)

    class Meta:
        model = Collection
        fields = '__all__'
        read_only_fields = ('movies', 'user', )


class MoviesListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('genres',)


class MoviesSerializer(serializers.ModelSerializer):
    collection_set = CollectionSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('genres')