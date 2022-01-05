from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
