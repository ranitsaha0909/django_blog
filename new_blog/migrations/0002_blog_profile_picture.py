# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='profile_picture',
            field=models.FileField(blank=True, upload_to='media/pictures/', null=True),
        ),
    ]
