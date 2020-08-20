from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=60)
    preferences = ArrayField(models.CharField(max_length=200), default=list)

    def __str__(self):
        return self.name

class Store(models.Model):
    store_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    products = ArrayField(models.CharField(max_length=200), default=list)

    def __str__(self):
        return self.store_name

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='users')
    store = models.ForeignKey(Store, on_delete=models.PROTECT, related_name='stores')
    products = ArrayField(models.CharField(max_length=200), default=list)