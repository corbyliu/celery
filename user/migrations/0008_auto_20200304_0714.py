# Generated by Django 2.1.8 on 2020-03-04 07:14

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_user_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]