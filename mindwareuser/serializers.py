from django.forms import widgets
from rest_framework import serializers
from models import *
class roleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = role
		fields = ('url','id','rolename')

class userSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = user
		fields = ('url','id','username','password','firstname','lastname','email','mobileno','role_id')
