# Generated by Django 3.0.7 on 2020-08-21 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0007_merge_20200821_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanhistory',
            name='scan_task_id',
            field=models.IntegerField(default=-1),
        ),
    ]
