from django.db import models
from django.utils.encoding import smart_unicode


class quiz(models.Model):
    quiz_name = models.CharField(max_length=200)  # Field name made lowercase.
    from_date = models.DateTimeField('From_date')  # Field name made lowercase.
    to_date = models.DateTimeField('To_date')  # Field name made lowercase.
    no_of_questions = models.IntegerField('No_of_questions')  # Field name made lowercase.
    no_of_games_for_a_day = models.CharField('No_of_games_for_a_day', max_length=20)  # Field name made lowercase.
    min_score = models.IntegerField('Min_score')  # Field name made lowercase.
    active_status = models.IntegerField('Active_status')  # Field name made lowercase.
    points_correct = models.IntegerField('Points_correct')  # Field name made lowercase.
    points_wrong = models.IntegerField('Points_wrong')  # Field name made lowercase.
    points_three_correct = models.IntegerField('Points_three_correct')  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.

    def __unicode__(self):
        return smart_unicode(self.quiz_name)
