# Generated by Django 2.1.8 on 2020-03-04 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200304_0359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='identifier',
        ),
    ]