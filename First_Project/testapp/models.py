from django.db import models

# Create your models here.
class Invoice(models.Model):
    seller=models.CharField(max_length=64)
    buyer=models.CharField(max_length=64)
    invoice_no = models.CharField(max_length=64)
    date = models.CharField(max_length=64)




