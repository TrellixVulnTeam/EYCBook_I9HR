# Generated by Django 2.2.3 on 2019-07-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0042_magazine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
