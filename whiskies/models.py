import django
from django.db import models

class Distillery(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    country = models.CharField(max_length=200, default='Scotland')
    author = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.DO_NOTHING)

class Whisky(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    distillery = models.ForeignKey(Distillery, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.DO_NOTHING)
