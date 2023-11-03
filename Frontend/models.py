from django.db import models


# Create your models here.
class contactDB(models.Model):
    FirstName = models.CharField(max_length=100, null=True, blank=True)
    LastName = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    City = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.CharField(max_length=100, null=True, blank=True)


class registerDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Username = models.CharField(max_length=100, null=True, blank=True)
    RegPassword = models.CharField(max_length=100, null=True, blank=True)


class Cartdb(models.Model):
    UserName = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(max_length=100, null=True, blank=True)
    TotalPrice = models.IntegerField(max_length=100, null=True, blank=True)
