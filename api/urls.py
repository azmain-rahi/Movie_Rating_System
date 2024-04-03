
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MovieViewSet, RatingViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'ratings', RatingViewSet, basename='rating')

urlpatterns = [
    path('', include(router.urls)),
]