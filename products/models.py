from django.db import models

# Create your models here.


class ProductType(models.Model):
    product_type = models.CharField('Tipo', max_length=50)

    def __str__(self):
        return self.product_type


class Product(models.Model):
    product_name = models.CharField('Producto', max_length=50)
    model = models.CharField('Modelo', max_length=50)
    type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    year = models.IntegerField('Año')
    price = models.FloatField('Precio')

    def __str__(self):
        return self.product_name
