from django.shortcuts import render
from serializers import *
from rest_framework import viewsets

class roleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = role.objects.all()
    serializer_class = roleSerializer

class userViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = user.objects.all()
    serializer_class = userSerializer