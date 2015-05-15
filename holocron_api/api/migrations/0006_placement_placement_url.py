# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20150506_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='placement',
            name='placement_url',
            field=models.CharField(default='www.carbonite.com', max_length=100),
            preserve_default=False,
        ),
    ]
