# Generated by Django 2.2.4 on 2019-09-23 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190923_1127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sales',
            options={'ordering': ['-date']},
        ),
    ]