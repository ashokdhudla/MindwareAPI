from django.shortcuts import render
from serializers import *
from rest_framework import viewsets

class promotionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = promotions.objects.all()
    serializer_class = promotionsSerializer