# Generated by Django 2.2.3 on 2019-07-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0007_auto_20190712_0648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='category',
        ),
        migrations.AddField(
            model_name='equipmentcategory',
            name='equipment',
            field=models.ManyToManyField(to='bio.Equipment'),
        ),
        migrations.AlterField(
            model_name='favoriteequipment',
            name='image',
            field=models.ImageField(max_length=300, upload_to='images/'),
        ),
    ]
