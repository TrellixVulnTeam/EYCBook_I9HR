# Generated by Django 2.2.3 on 2019-07-12 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0012_auto_20190712_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='categoryId',
            new_name='category',
        ),
    ]
