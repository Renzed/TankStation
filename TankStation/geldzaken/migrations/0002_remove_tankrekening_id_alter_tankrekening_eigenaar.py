# Generated by Django 4.1.4 on 2023-01-01 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geldzaken', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tankrekening',
            name='id',
        ),
        migrations.AlterField(
            model_name='tankrekening',
            name='eigenaar',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
