# Generated by Django 3.1.3 on 2020-12-09 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0023_auto_20201202_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controllertask',
            name='controller_component',
            field=models.ForeignKey(help_text='On which controller this task is executed.', on_delete=django.db.models.deletion.CASCADE, related_name='controller_task_set', to='farms.controllercomponent'),
        ),
        migrations.AlterField(
            model_name='controllertask',
            name='parameters',
            field=models.JSONField(blank=True, default=dict, help_text="The setup parameters excl. the task's ID, state and type. Theperipheral ID parameter has to use the peripheral component's ID instead thatof its site entity."),
        ),
        migrations.AlterField(
            model_name='peripheralcomponent',
            name='parameters',
            field=models.JSONField(default=dict, help_text="The setup parameters excl. the peripheral's ID, state, type and data point type parameters."),
        ),
    ]