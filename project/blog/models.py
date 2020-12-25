from django.db import models
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=255,blank=True,null=True)
    desc=models.TextField(blank=True,null=True)
    url=models.TextField(blank=True,null=True)
    slug=models.SlugField(max_length=300,null=True)
   
       
    def save(self):
        self.slug=slugify(self.title)
        super(Post,self).save()
        
    def __str__(self):
        return '%s' % self.title
