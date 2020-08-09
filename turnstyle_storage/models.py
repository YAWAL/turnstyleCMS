from django.db import models


class Material(models.Model):
    type = models.CharField(max_length=30)
    standard = models.CharField(max_length=30)
    coating = models.CharField(max_length=30)


class Turnstyle(models.Model):
    articyl = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    material = models.ForeignKey(Material, on_delete=models.DO_NOTHING)
    price = models.IntegerField()
    type = models.CharField(max_length=30)
    produce_date = models.DateTimeField("manufacturing date")


