# Generated by Django 3.0.3 on 2021-03-02 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agreement', '0044_person_entry_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='entry_by',
        ),
        migrations.AddField(
            model_name='site',
            name='entry_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
