from django.db import models


# Create your models here.
class shopDB(models.Model):
    CategoryName = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    CategoryImage = models.ImageField(upload_to="CategoryImage", null=True, blank=True)


class productDB(models.Model):
    CategoryName = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    ProductImage = models.ImageField(upload_to="ProductImage", null=True, blank=True)


