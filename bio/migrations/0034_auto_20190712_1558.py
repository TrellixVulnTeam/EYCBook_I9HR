# Generated by Django 2.2.3 on 2019-07-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0033_auto_20190712_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='image',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='favoriteequipment',
            name='image',
            field=models.TextField(),
        ),
    ]
