from django.db import models

# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=20,default='null')
    author=models.CharField(max_length=20,default='unknown')
    seller=models.CharField(max_length=20,default='unknown')
    price=models.FloatField(max_length=3,default=0.0)
    description=models.TextField(default='Nothing')

class Comment(models.Model):
    bookid=models.IntegerField(default=0)
    user=models.CharField(max_length=20,default='unknown')
    time=models.DateTimeField(auto_now_add=True)
    content=models.TextField(default='Nothing')
    rank=models.IntegerField(default=-1)

