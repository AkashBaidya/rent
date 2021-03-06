# Generated by Django 3.0.3 on 2021-03-04 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agreement', '0054_auto_20210304_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='agreement_cat_type',
            field=models.CharField(choices=[('Relocation', 'Relocation'), ('New', 'New'), ('Old', 'Old'), ('Renewal', 'Renewal'), ('Extension', 'Extension'), ('Additional Space', 'Additional Space'), ('Amendment Of Lease Agreement -Sep-2019', 'Amendment Of Lease Agreement -Sep-2019'), ('Ground floor', 'Ground floor'), ('Possession purchase', 'Possession purchase'), ('Renewal(Extension)', 'Renewal(Extension)'), ('Space-Extension', 'Space-Extension')], max_length=90, verbose_name='Agreement category type'),
        ),
    ]
