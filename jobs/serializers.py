from django.forms import widgets
from rest_framework import serializers
from models import *

class jobSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = job
		fields = ('url','job_title','description','department_id','expiry_date')

class job_applicationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = job_application
		fields = ('url','job_app_id','ja_user_id','ja_job_id')

class job_departmentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = job_department
		fields = ('url','dep_name')

