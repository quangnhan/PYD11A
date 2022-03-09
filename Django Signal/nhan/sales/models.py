from django.db import models
from orders.models import Order

# Create your models here.

class Sale(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return str(self.amount)