# Generated by Django 2.2 on 2020-09-07 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niza', '0005_projectfile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttask',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]