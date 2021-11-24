# Generated by Django 3.2.9 on 2021-11-24 21:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CoursesApp', '0002_courses_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courses',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Updated'),
            preserve_default=False,
        ),
    ]
