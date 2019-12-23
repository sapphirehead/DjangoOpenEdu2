"""
Definition of models.
"""

from django.db import models
from django.contrib import admin # use admin's module
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = 'posted',
                             verbose_name = 'Title')
    descriptions = models.TextField(verbose_name = 'Summary' )
    content = models.TextField(verbose_name = 'Full content' )
    posted = models.DateTimeField(default = datetime.now(), db_index = True,
                                  verbose_name = 'Publiced')
    author = models.ForeignKey(User, null=True, blank=True, 
                               on_delete = models.SET_NULL, 
                               verbose_name = "Author")
    image = models.FileField(default = 'temp.jpg', 
                             verbose_name = 'Path to image')
    
    def get_absolute_url(self): # return string with unique url note
        return reverse('blogpost', args=[str(self.id)])

    def __str__(self): # return name for different notes
        return self.title

    class Meta:
        db_table = 'Posts' # name of database table for model
        ordering = ['-posted'] # order by sort data in model (- means by decrease)
        verbose_name = 'article' # model's name for showing on the admin's page
        verbose_name_plural = 'blog\'s articles' # too for all blog's articles

class Comment(models.Model):
    text = models.TextField(null=True, verbose_name = 'Comment')
    date = models.DateTimeField(default = datetime.now(), 
                                db_index = True, 
                                verbose_name = 'Date')
    post = models.ForeignKey(Blog, null=True, blank=True, on_delete = models.CASCADE,
                             verbose_name = 'Article')
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.CASCADE, 
                               verbose_name = 'Comment\'s Author')
    
    def __str__(self): # return comments for different notes
        #return 'Comment %s -> %s' % (self.author, self.post)
        return 'Comment {} -> {}'.format(self.author, self.post)

    class Meta:
        db_table = 'Comments' # name of database table for model
        ordering = ['-date'] # order by sort data in model (- means by decrease)
        verbose_name = 'comment' # model's name for showing on the admin's page
        verbose_name_plural = 'comments of blog\s articles' # too for all blog's articles

admin.site.register(Blog)
admin.site.register(Comment)