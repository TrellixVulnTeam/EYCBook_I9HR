# Generated by Django 2.2.3 on 2019-07-12 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0010_auto_20190712_0756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoriteequipment',
            name='created',
        ),
        migrations.RemoveField(
            model_name='favoriteequipment',
            name='updated',
        ),
    ]
