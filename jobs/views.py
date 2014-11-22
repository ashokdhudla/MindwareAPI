from django.shortcuts import render
from serializers import *
from rest_framework import viewsets

class jobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = job.objects.all()
    serializer_class = jobSerializer

class job_applicationViewSet(viewsets.ModelViewSet):

	queryset = job_application.objects.all()
	serializer_class = job_applicationSerializer
	
class job_departmentViewSet(viewsets.ModelViewSet):

	queryset = job_department.objects.all()
	serializer_class = job_departmentSerializer