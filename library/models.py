from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    seller=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=3,decimal_places=2)
    description=models.TextField()
