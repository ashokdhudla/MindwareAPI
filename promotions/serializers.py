from django.forms import widgets
from rest_framework import serializers
from models import *

class promotionsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = promotions
		fields = ('url','promo_name','description','image','start_date','end_date')
