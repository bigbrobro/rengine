# Generated by Django 3.0.7 on 2020-07-15 16:35

from django.db import migrations
import yamlfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scanEngine', '0008_auto_20200715_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enginetype',
            name='yaml_configuration',
            field=yamlfield.fields.YAMLField(default=''),
        ),
    ]