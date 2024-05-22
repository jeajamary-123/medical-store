from django.db import models


class med_kit(models.Model):
    Medname = models.CharField(max_length=500)
    Description = models.TextField()                                                   
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Quantity =  models.CharField(max_length=50)