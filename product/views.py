from django.shortcuts import render
from serializers import *
from rest_framework import viewsets

class productViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = product.objects.all()
    serializer_class = productSerializer

class product_categoriesViewSet(viewsets.ModelViewSet):

	queryset = product_categories.objects.all()
	serializer_class = product_categoriesSerializer

class brandViewSet(viewsets.ModelViewSet):
	queryset = brand.objects.all()
	serializer_class = brandSerializer
