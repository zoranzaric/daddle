# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('daddle', '0002_pledge'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='event',
            field=models.ForeignKey(default=1, to='daddle.Event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pledge',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
