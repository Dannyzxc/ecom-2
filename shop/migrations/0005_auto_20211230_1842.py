# Generated by Django 3.2.6 on 2021-12-30 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='email',
            field=models.CharField(default='', max_length=110),
        ),
    ]
