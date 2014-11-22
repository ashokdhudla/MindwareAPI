from django.forms import widgets
from rest_framework import serializers
from models import *

class quizSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = quiz
		fields = ('url','quiz_name','from_date','to_date','no_of_questions','no_of_games_for_a_day','min_score','active_status','points_correct','points_wrong','points_three_correct')
