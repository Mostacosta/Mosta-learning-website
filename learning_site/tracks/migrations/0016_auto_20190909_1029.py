# Generated by Django 2.2.3 on 2019-09-09 17:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0015_exam_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_result',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
