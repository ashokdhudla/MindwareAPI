from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.
class role(models.Model):
	rolename = models.CharField(max_length=25)
	created_at = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return smart_unicode(self.rolename)
class user(models.Model):
	username = models.CharField(max_length=50, null=True)
	password = models.CharField(max_length=20)
	firstname = models.CharField(max_length=60, null=True)
	lastname = models.CharField(max_length=60, null = True)
	email = models.EmailField(max_length=255)
	mobileno = models.CharField(max_length=15,null = True)
	role_id = models.ForeignKey('role')
	created_at = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return smart_unicode(self.username)
