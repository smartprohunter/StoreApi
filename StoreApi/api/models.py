from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Order(models.Model):
    date = models.DateField()
    products = models.ManyToManyField(Product)
