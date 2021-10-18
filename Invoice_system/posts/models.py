from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Invoice(models.Model):
    Invoice_Id =models.TextField(max_length=10)
    Invoice_date=models.DateTimeField(auto_now_add=True)
    total_cost=models.FloatField(default=0)
    def __str__(self):
        return self.Invoice_Id
         

class Items(models.Model):
    Invoice_no = models.ForeignKey(Invoice, on_delete=models.CASCADE,related_name='Invoice_no')
    Cost = models.FloatField()
    description = models.TextField()
    def __str__(self):
        return self.description

