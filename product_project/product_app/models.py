from django.db import models


class Product(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=30)
    product_category = models.CharField(max_length=20)
    product_price = models.FloatField()
    product_manufacturing_date = models.DateField()
    product_manufactured_by = models.CharField(max_length=30)
