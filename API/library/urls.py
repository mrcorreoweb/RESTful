"""Set up the url routes for the library application."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WriterViewSet, BookViewSet

# Create a router and register the ViewSets
router = DefaultRouter()
router.register(r'writers', WriterViewSet, basename='writer')
router.register(r'books', BookViewSet, basename='book')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
