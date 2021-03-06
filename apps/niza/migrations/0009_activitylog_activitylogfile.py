# Generated by Django 2.2 on 2020-09-08 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('niza', '0008_auto_20200907_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='niza.Project')),
            ],
            options={
                'verbose_name': 'Activity Log',
                'verbose_name_plural': 'Activities Logs',
            },
        ),
        migrations.CreateModel(
            name='ActivityLogFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='project_files')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='niza.ActivityLog')),
            ],
            options={
                'verbose_name': 'Activity Log File',
                'verbose_name_plural': 'Activities Logs File',
            },
        ),
    ]
