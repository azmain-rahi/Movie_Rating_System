from django.shortcuts import render

# Create your views here.

# api/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Movie, Rating
from .serializers import UserSerializer, MovieSerializer, RatingSerializer
from accounts.models import CustomUser  # Import the CustomUser model


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['get'])
    def ratings(self, request, pk=None):
        movie = self.get_object()
        ratings = Rating.objects.filter(movie=movie)
        serializer = RatingSerializer(ratings, many=True)
        average_rating = sum(rating.rating for rating in ratings) / len(ratings) if ratings else 0
        return Response({'ratings': serializer.data, 'average_rating': average_rating})

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        movie_id = request.data.get('movie')
        if not movie_id:
            return Response({'error': 'Movie ID is required.'}, status=400)

        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found.'}, status=404)

        rating = request.data.get('rating')
        if rating is None or rating < 0 or rating > 5:
            return Response({'error': 'Invalid rating value.'}, status=400)

        existing_rating = Rating.objects.filter(user=user, movie=movie).first()
        if existing_rating:
            existing_rating.rating = rating
            existing_rating.save()
            return Response({'message': 'Rating updated successfully.'}, status=200)

        serializer = self.get_serializer(data={'user': user.id, 'movie': movie_id, 'rating': rating})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Rating added successfully.'}, status=201)
