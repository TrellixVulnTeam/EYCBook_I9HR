# Generated by Django 2.2.3 on 2019-07-12 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0026_auto_20190712_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creator',
            name='slug',
        ),
    ]
