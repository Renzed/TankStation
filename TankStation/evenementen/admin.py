from django.contrib import admin

# Register your models here.

from .models import Tanktiviteit, Inschrijving

admin.site.register(Tanktiviteit)
admin.site.register(Inschrijving)
