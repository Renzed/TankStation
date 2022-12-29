from django.urls import path

from . import views

app_name = "geldzaken"
urlpatterns = [
    path('', views.index, name='Geld home')
]