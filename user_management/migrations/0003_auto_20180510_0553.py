# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_post_user_unq_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_unq_id',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=15, unique=True),
        ),
    ]
