# Generated by Django 2.2.2 on 2019-06-20 21:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='posted_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 6, 20, 18, 53, 51, 446918)),
            preserve_default=False,
        ),
    ]
