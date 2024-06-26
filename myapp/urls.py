from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet  # Import your viewset from views.py within the same app

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'items', ItemViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

