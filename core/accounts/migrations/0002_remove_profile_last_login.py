# Generated by Django 2.1.5 on 2019-01-29 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_login',
        ),
    ]
