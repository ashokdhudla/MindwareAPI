from django.db import models
from django.utils.encoding import smart_unicode


class survey(models.Model):
    survey_name = models.CharField(max_length=400)
    num_of_questions = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.

    def __unicode__(self):
        return smart_unicode(self.survey_name)

class survey_options(models.Model):
    option_details = models.CharField(max_length=400)
    question_id = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.

    def __unicode__(self):
        return smart_unicode(self.option_details)

class survey_questions(models.Model):
    question_details = models.CharField(max_length=400)
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    d = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    survey_id = models.ForeignKey('survey')
    created_at = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    def __unicode__(self):
        return smart_unicode(self.question_details)
    
class survey_response(models.Model):
    response_option = models.CharField(max_length=20)
    user_id = models.IntegerField()
    question_id = models.IntegerField()
    submitted_at = models.DateTimeField('Submitted_at')  # Field name made lowercase.

    def __unicode__(self):
        return smart_unicode(self.response_option)