from django.forms import widgets
from rest_framework import serializers
from product.models import *

class productSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = product
		fields = ('url','id','name','description','brand_id','image','cat_id')

class brandSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = brand
		fields = ('url','id','brand_name')

class product_categoriesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = product_categories
		fields = ('url','id','category')
