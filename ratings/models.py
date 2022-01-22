import django
from django.db import models

import whiskies


class Rating(models.Model):
    whisky = models.ForeignKey('whiskies.Whisky', on_delete=models.DO_NOTHING)
    nose = models.FloatField()
    taste = models.FloatField()
    color = models.IntegerField()
    smokiness = models.IntegerField()
    date = models.DateField()
    author = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.DO_NOTHING)
