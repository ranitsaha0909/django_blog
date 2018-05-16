# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_auto_20180510_0553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user_unq_id',
        ),
    ]
