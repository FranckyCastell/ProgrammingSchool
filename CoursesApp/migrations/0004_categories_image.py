# Generated by Django 3.2.9 on 2021-11-25 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoursesApp', '0003_auto_20211124_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Categories', verbose_name='Image'),
        ),
    ]
