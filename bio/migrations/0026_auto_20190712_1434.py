# Generated by Django 2.2.3 on 2019-07-12 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0025_auto_20190712_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='favoriteequipment',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
