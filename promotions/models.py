from django.db import models
from django.utils.encoding import smart_unicode


def Content_files(instance, filename):
    return '/'.join(['Media','Promotion Image', filename])

class promotions(models.Model):
    promo_name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    image = models.FileField(upload_to=Content_files)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.

    def __unicode__(self):
        return smart_unicode(self.promo_name)