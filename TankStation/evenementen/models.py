from django.db import models
from django.conf import settings

# Create your models here.


class Tanktiviteit(models.Model):
    naam = models.CharField(max_length=140)
    beschrijving = models.CharField(max_length=400)
    prijs = models.DecimalField("Prijs", max_digits=7, decimal_places=2, default=0.00)
    gemaakt_door = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="Gemaakt_door")
    verantwoordelijke = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="Verantwoordelijke")
    aanmaakmoment = models.DateTimeField("Aangemaakt op", auto_now_add=True)
    sluiting = models.DateTimeField("De inschrijvingen sluiten om")
    wanneer = models.DateTimeField("Tanktiviteit moment")
    plaatje = models.ImageField(upload_to="images/", default="images/tank.jpg")
    max_inschrijvingen = models.PositiveSmallIntegerField(default=76)


class Inschrijving(models.Model):
    plaatser = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="inschrijvingen", on_delete=models.CASCADE, null=True)
    tanktiviteit = models.ForeignKey(Tanktiviteit, related_name="inschrijvingen", on_delete=models.CASCADE)
    opmerkingen = models.CharField(max_length=140)
