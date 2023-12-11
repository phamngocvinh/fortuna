from django.db import models


class BingoCard(models.Model):
    userid = models.CharField(max_length=200)
    date = models.CharField(max_length=8)
    numbers = models.CharField(max_length=200)
    create_datetime = models.DateTimeField(null=True)


class System(models.Model):
    lock_submit = models.IntegerField(default=0)
