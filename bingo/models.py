from django.db import models


class Account(models.Model):
    account_name = models.CharField(max_length=100)
    create_datetime = models.DateTimeField("datetime created")


class BingoCard(models.Model):
    account_name = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField("date created")
    col_1 = models.CharField(max_length=20)
    col_2 = models.CharField(max_length=20)
    col_3 = models.CharField(max_length=20)
    col_4 = models.CharField(max_length=20)
    col_5 = models.CharField(max_length=20)
