# Generated by Django 2.2 on 2020-09-11 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('niza', '0009_activitylog_activitylogfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerreview',
            name='customer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='niza.Customer'),
        ),
    ]
