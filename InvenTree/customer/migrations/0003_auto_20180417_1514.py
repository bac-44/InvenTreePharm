# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20180418_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorderline',
            name='customer_order',
            field=models.ForeignKey(help_text=b'Order this line belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='customer.CustomerOrder'),
        ),
        migrations.AlterField(
            model_name='customerorderline',
            name='part',
            field=models.ForeignKey(blank=True, help_text=b'Part', on_delete=django.db.models.deletion.CASCADE, to='part.Part'),
        ),
    ]
