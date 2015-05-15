# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150506_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='end_date',
            field=models.DateField(verbose_name=b'End Date'),
        ),
    ]
