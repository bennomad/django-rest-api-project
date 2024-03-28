from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        """
        Optionally restricts the returned items to a given name,
        by filtering against a `name` query parameter in the URL.
        """
        queryset = Item.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
