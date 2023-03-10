# Generated by Django 4.1.4 on 2023-01-02 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geldzaken', '0002_remove_tankrekening_id_alter_tankrekening_eigenaar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oplading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedrag', models.DecimalField(decimal_places=2, max_digits=7)),
                ('wanneer', models.DateTimeField(auto_now_add=True)),
                ('tankrekening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opladingen', to='geldzaken.tankrekening')),
            ],
        ),
    ]
