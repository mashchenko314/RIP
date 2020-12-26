from django.db import models


class Bouquet(models.Model):
    name = models.CharField(max_length=20)


class Description(models.Model):
    bouquet_id = models.ForeignKey(Bouquet, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)