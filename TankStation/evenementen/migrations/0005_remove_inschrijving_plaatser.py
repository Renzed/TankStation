# Generated by Django 4.1.4 on 2022-12-26 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evenementen', '0004_tanktiviteit_beschrijving_tanktiviteit_gemaakt_door_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inschrijving',
            name='plaatser',
        ),
    ]