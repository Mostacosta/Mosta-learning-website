# Generated by Django 2.2.3 on 2019-09-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0016_auto_20190909_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam_result',
            name='case',
            field=models.CharField(choices=[('failed', 'failed'), ('success', 'success')], default='failed', max_length=20),
        ),
    ]
