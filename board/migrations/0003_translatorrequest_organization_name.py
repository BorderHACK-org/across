# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20151122_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='translatorrequest',
            name='organization_name',
            field=models.CharField(max_length=64, blank=True),
        ),
    ]
