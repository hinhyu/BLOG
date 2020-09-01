from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    body = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title