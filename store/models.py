from django.db import models
from account.models import Account

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Form(models.Model):
    customer = models.ForeignKey(
        Account, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    notes = models.CharField(max_length=200, null=True)
    fufilled = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return str(self.id)


class Formitems(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True)
    form = models.ForeignKey(
        Form, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
