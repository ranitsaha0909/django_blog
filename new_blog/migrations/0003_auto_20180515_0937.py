# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_blog', '0002_blog_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='profile_picture',
            new_name='picture',
        ),
    ]
