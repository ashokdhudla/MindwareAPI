from django.db import models
from django.utils.encoding import smart_unicode

class brand(models.Model):
    brand_name = models.CharField(db_column='Brand_name', max_length=100)  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    def __unicode__(self):
       return smart_unicode(self.brand_name)

class product_categories(models.Model):
    category = models.CharField(db_column='Category', max_length=100)  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    def __unicode__(self):
       return smart_unicode(self.category)

def Content_files(instance, filename):
    return '/'.join(['Media','Product Image', filename])

class product(models.Model):
    name = models.CharField('Product Name',max_length=200)  # Field name made lowercase.
    description = models.TextField('Description')  # Field name made lowercase.
    brand_id = models.ForeignKey('brand')  # Field name made lowercase.
    image = models.FileField(upload_to = Content_files)  # Field name made lowercase.
    cat_id = models.ForeignKey('product_categories')  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)  # Field name made lowercase.
    def __unicode__(self):
       return smart_unicode(self.name)


