# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_tracking', '0004_add_verbose_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='apirequestlog',
            name='authentication',
            field=models.CharField(max_length=200, null=True, blank=True)
        ),
    ]
