# Generated by Django 2.2 on 2020-09-07 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niza', '0007_auto_20200907_0851'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projecttask',
            options={'ordering': ['-order'], 'verbose_name': 'Project Task', 'verbose_name_plural': 'Project Tasks'},
        ),
        migrations.AddField(
            model_name='projecttask',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]