# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20151130_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='f2f_url',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
