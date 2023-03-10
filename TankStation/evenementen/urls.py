from django.urls import path

from . import views

app_name = 'evenementen'
urlpatterns = [
    path('', views.index, name="Evenementen home"),
    path('detail/<int:tanktiviteit_id>', views.detail, name="Tanktiviteit detail"),
    path('detail/<int:tanktiviteit_id>/inschrijven', views.inschrijven, name="Inschrijven"),
    path('detail/<int:tanktiviteit_id>/uitschrijven/<int:inschrijving_id>', views.uitschrijven, name='Uitschrijven'),
    path('geweest/<int:pagesize>/<int:page>', views.geweest, name="Geweeste tanktiviteiten")
]
