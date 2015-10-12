# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daddle', '0003_auto_20151012_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='cancel_timestamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
