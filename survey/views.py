from django.shortcuts import render
from serializers import *
from rest_framework import viewsets

class surveyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = survey.objects.all()
    serializer_class = surveySerializer

class survey_optionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = survey_options.objects.all()
    serializer_class = survey_optionsSerializer

class survey_questionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = survey_questions.objects.all()
    serializer_class = survey_questionsSerializer

class survey_responseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = survey_response.objects.all()
    serializer_class = survey_responseSerializer