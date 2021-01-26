# Generated by Django 3.0.5 on 2020-04-07 12:30

import address.models
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import macaddress.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0002_auto_20160213_1726'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Controller',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The UUID to identify the controller.', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, help_text='The name of the controller', max_length=30, null=True)),
                ('wifi_mac_address', macaddress.fields.MACAddressField(help_text='The Wifi MAC address of the controller.', integer=True)),
                ('external_ip_address', models.GenericIPAddressField(help_text='The external IP address of the controller.')),
                ('controller_type', models.CharField(choices=[('PUM', 'Pump controller'), ('DOS', 'Dosage controller'), ('CAM', 'Camera controller'), ('SEN', 'Sensor controller'), ('UNK', 'Unknown controller')], default='UNK', help_text='The main function of the controller (e.g., pump or sensor controller).', max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the controller was first registered.')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='The date and time when the controller was last updated.')),
            ],
        ),
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The UUID to identify the hydroponic system.', primary_key=True, serialize=False)),
                ('local_ip_address', models.GenericIPAddressField(help_text="The coordinator's local IP address.")),
                ('external_ip_address', models.GenericIPAddressField(help_text="The coordinator's external IP address.")),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the coordinator was first registered.')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='The date and time when the coordinator was last updated.')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The UUID to identify the hydroponic system.', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='The name of the site.', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the site was first created.')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='The date and time when the site was last updated.')),
                ('address', address.models.AddressField(help_text='The postal address and the coordinates of the site', null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.Address')),
                ('owner', models.ForeignKey(help_text='The user that owns the site.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MqttMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='The datetime when the message was received')),
                ('message', django.contrib.postgres.fields.jsonb.JSONField()),
                ('topic_prefix', models.CharField(choices=[('cmd', 'Command topic'), ('tel', 'Telemetry topic'), ('reg', 'Register topic')], help_text='The purpose of the message.', max_length=3)),
                ('topic_suffix', models.CharField(help_text='The context of the message.', max_length=30)),
                ('controller', models.ForeignKey(blank=True, help_text='If not None, the sender of the message.', null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.Controller')),
                ('coordinator', models.ForeignKey(help_text='The coordinator that relayed the message.', on_delete=django.db.models.deletion.CASCADE, to='farms.Coordinator')),
            ],
        ),
        migrations.CreateModel(
            name='HydroponicSystem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The UUID to identify the hydroponic system.', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, help_text='The name of the hydroponic system', max_length=30, null=True)),
                ('system_type', models.CharField(choices=[('VT', 'Vertical tower'), ('FD', 'Flood and drain'), ('NFT', 'Nutrient film technique'), ('DWC', 'Deep water culture')], default='VT', help_text="The hydroponic system's type (e.g., vertical tower, flood and drain).", max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the hydroponic system was first registered.')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='The date and time when the hydroponic system was last updated.')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.Site')),
            ],
        ),
        migrations.AddField(
            model_name='coordinator',
            name='site',
            field=models.ForeignKey(blank=True, help_text='The site to which the coordinator belongs.', null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.Site'),
        ),
        migrations.AddField(
            model_name='controller',
            name='coordinator',
            field=models.ForeignKey(help_text='The coordinator with which the controller is connected to.', null=True, on_delete=django.db.models.deletion.CASCADE, to='farms.Coordinator'),
        ),
    ]