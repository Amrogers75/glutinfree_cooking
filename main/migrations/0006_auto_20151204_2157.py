# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20151203_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(default=1, upload_to=b'media_folder'),
            preserve_default=False,
        ),
    ]
