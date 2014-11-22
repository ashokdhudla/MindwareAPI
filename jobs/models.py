from django.db import models
from django.utils.encoding import smart_unicode

class job(models.Model):
    job_title = models.CharField(max_length=200)  # Field name made lowercase.
    description = models.TextField('Description')  # Field name made lowercase.
    department_id = models.ForeignKey('job_department')  # Field name made lowercase.
    expiry_date = models.DateField('Expiry_date')  # Field name made lowercase.
    # status = models.IntegerField('Status')  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    def __unicode__(self):
        return smart_unicode(self.job_title)


class job_application(models.Model):
    job_app_id = models.IntegerField(primary_key=True)
    ja_user_id = models.IntegerField()
    ja_job_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return smart_unicode(self.job_app_id)


class job_department(models.Model):
    dep_name = models.CharField(max_length=200)  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.

    def __unicode__(self):
        return smart_unicode(self.dep_name)


