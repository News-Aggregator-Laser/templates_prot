from unicodedata import category
from django.db import models

# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=350)
    content = models.TextField()
    category = models.CharField(max_length=100)
    image_url = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    published_at = models.DateTimeField()
    top_new = models.BooleanField(default=False)
    top_in_category = models.BooleanField(default=False)

    def __str__(self):
        return self.title
