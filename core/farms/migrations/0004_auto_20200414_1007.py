# Generated by Django 3.0.5 on 2020-04-14 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0003_auto_20200412_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mqttmessage',
            name='topic_suffix',
            field=models.CharField(default='', help_text='The context of the message.', max_length=30),
        ),
    ]
