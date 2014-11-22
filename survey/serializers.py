from django.forms import widgets
from rest_framework import serializers
from models import *

class surveySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = survey
		fields = ('url','survey_name','num_of_questions')

class survey_optionsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = survey_options
		fields = ('url','option_details','question_id')

class survey_questionsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = survey_questions
		fields = ('url','question_details','a','b','c','d','survey_id')

class survey_responseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = survey_response
		fields = ('url','response_option','user_id','question_id','submitted_at')