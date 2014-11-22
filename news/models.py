from django.db import models
from django.utils.encoding import smart_unicode

class news_categories(models.Model):
    cat_name = models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return smart_unicode(self.cat_name)

def Content_files(instance, filename):
    return '/'.join(['Media','News Image', filename])

class news(models.Model):
    name = models.CharField(max_length=30,null=True)
    description = models.TextField()
    cat_id = models.ForeignKey('news_categories')
    image = models.FileField(upload_to=Content_files)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
       return smart_unicode(self.name)
