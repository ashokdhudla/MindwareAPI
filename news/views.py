from django.shortcuts import render
from serializers import *
from rest_framework import viewsets

class newsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = news.objects.all()
    serializer_class = newsSerializer

class news_categoriesViewSet(viewsets.ModelViewSet):

	queryset = news_categories.objects.all()
	serializer_class = news_categoriesSerializer