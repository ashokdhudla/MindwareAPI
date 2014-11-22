from django.shortcuts import render
from serializers import *
from rest_framework import viewsets

class quizViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = quiz.objects.all()
    serializer_class = quizSerializer