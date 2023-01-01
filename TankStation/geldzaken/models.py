from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class TankRekening(models.Model):
    eigenaar = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    geverifieerd_saldo = models.DecimalField(max_digits=7, decimal_places=2)
    geverifieerd_op = models.DateTimeField()

    def uit_gaan_geven(self):
        ingeschreven_ttvt = self.eigenaar.inschrijvingen.filter(tanktiviteit__wanneer__gt=timezone.now(),
                                                                tanktiviteit__tankrekening=True)
        ugg = 0
        for ins in ingeschreven_ttvt:
            ugg += ins.tanktiviteit.prijs
        return ugg

    def uitgegegeven(self):
        ingeschreven_ttvt = self.eigenaar.inschrijvingen.filter(tanktiviteit__wanneer__range=[self.geverifieerd_op,
                                                                                              timezone.now()],
                                                                tanktiviteit__tankrekening=True)
        ugg = 0
        for ins in ingeschreven_ttvt:
            ugg += ins.tanktiviteit.prijs
        return ugg

    def saldo(self):
        return self.geverifieerd_saldo-self.uitgegegeven()

    def inschrijvingen(self, uitgave):
        if uitgave:
            return self.eigenaar.inschrijvingen.filter(tanktiviteit__tankrekening=True)
        else:
            return self.eigenaar.inschrijvingen.all()
