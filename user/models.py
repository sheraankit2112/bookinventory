
from django.db import models

class userdetail(models.Model):
    username=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    store=models.CharField(max_length=20)

class books(models.Model):
    username=models.CharField(max_length=20)
    store=models.CharField(max_length=20)
    book=models.CharField(max_length=30)
    author=models.CharField(max_length=40)
    counts=models.IntegerField(max_length=20)
    price=models.IntegerField(max_length=20)