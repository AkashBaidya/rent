# Generated by Django 3.0.3 on 2021-03-02 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agreement', '0046_auto_20210302_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='last_modified_by',
        ),
    ]