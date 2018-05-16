# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_unq_id',
            field=models.CharField(blank=True, default=uuid.uuid4, unique=True, max_length=100),
        ),
    ]
