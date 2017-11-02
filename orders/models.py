from django.db import models

# Create your models here.

class Order(models.Model):
    book_id=models.IntegerField()
    customer=models.CharField(max_length=20)
    ordertime=models.DateTimeField(auto_now_add=True)
    dealt=models.BooleanField(default=False)


