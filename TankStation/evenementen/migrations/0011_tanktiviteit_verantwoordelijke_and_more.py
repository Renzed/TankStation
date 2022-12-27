# Generated by Django 4.1.4 on 2022-12-27 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evenementen', '0010_tanktiviteit_max_inschrijvingen'),
    ]

    operations = [
        migrations.AddField(
            model_name='tanktiviteit',
            name='verantwoordelijke',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Verantwoordelijke', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tanktiviteit',
            name='gemaakt_door',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Gemaakt_door', to=settings.AUTH_USER_MODEL),
        ),
    ]
