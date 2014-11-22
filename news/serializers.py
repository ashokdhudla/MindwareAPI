from django.forms import widgets
from rest_framework import serializers
from models import *

class newsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = news
		fields = ('url','id','name','description','cat_id','image','date')

class news_categoriesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = news_categories
		fields = ('url','id','cat_name')
