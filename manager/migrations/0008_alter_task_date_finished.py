# Generated by Django 4.0.3 on 2022-03-25 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_alter_task_date_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_finished',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
