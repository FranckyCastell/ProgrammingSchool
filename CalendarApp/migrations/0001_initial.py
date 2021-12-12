# Generated by Django 3.2.9 on 2021-12-12 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Título')),
                ('start', models.CharField(blank=True, default='2021-12-11T22:30:00', max_length=20, null=True, verbose_name='Data Inicio')),
                ('end', models.CharField(blank=True, default='2021-12-11T22:30:00', max_length=20, null=True, verbose_name='Data Final')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL Google Meet')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
    ]
