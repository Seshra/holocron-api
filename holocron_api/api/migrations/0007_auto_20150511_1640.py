# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_placement_placement_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='campaign_description',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='content',
            name='content_description',
            field=models.CharField(max_length=140),
        ),
    ]
