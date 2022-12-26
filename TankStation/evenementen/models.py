from django.db import models
from django.conf import settings

# Create your models here.


class Tanktiviteit(models.Model):
    naam = models.CharField(max_length=140)
    beschrijving = models.CharField(max_length=400)
    prijs = models.FloatField()
    gemaakt_door = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    aanmaakmoment = models.DateTimeField("Aangemaakt op", auto_now_add=True)
    sluiting = models.DateTimeField("De inschrijvingen sluiten om")
    wanneer = models.DateTimeField("Tanktiviteit moment")


class Inschrijving(models.Model):
    # plaatser = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="inschrijvingen", on_delete=models.CASCADE)
    tanktiviteit = models.ForeignKey(Tanktiviteit, related_name="inschrijvingen", on_delete=models.CASCADE)
    opmerkingen = models.CharField(max_length=140)
