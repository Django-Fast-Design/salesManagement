# Generated by Django 2.1.7 on 2019-08-18 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190811_2238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
    ]
