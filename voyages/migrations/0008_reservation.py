# Generated by Django 4.1.5 on 2023-01-19 00:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voyages', '0007_alter_hotel_localisation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reservation', models.DateField(default=datetime.date.today)),
                ('sejour', models.IntegerField()),
                ('Hotel', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='voyages.hotel')),
                ('Transport', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='voyages.transport')),
                ('voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyages.voyage')),
            ],
        ),
    ]
