# Generated by Django 3.0.3 on 2021-03-04 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreement', '0048_auto_20210302_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sis_supplier_code',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
