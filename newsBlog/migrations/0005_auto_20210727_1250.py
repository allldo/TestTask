# Generated by Django 3.2.5 on 2021-07-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsBlog', '0004_alter_news_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='IP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IpName', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.ManyToManyField(blank=True, to='newsBlog.IP'),
        ),
    ]