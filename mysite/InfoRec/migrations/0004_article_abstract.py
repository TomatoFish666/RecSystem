# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoRec', '0003_auto_20160323_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='abstract',
            field=models.TextField(blank=True, verbose_name='摘要'),
        ),
    ]
