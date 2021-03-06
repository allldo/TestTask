# Generated by Django 3.2.5 on 2021-07-27 05:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newsBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(blank=True, to='newsBlog.Tag'),
        ),
        migrations.AddField(
            model_name='tag',
            name='TagName',
            field=models.CharField(default=datetime.datetime(2021, 7, 27, 5, 18, 23, 785949, tzinfo=utc), max_length=65),
            preserve_default=False,
        ),
    ]
