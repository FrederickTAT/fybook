from django.db import models

# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=20,default='null')
    author=models.CharField(max_length=20,default='unknown')
    seller=models.CharField(max_length=20,default='unknown')
    price=models.FloatField(max_length=3,default=0.0)
    description=models.TextField(default='')


    def __str__(self):
        return self.title
