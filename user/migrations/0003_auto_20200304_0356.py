# Generated by Django 2.1.8 on 2020-03-04 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200304_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(help_text='电话号码', max_length=11),
        ),
    ]
