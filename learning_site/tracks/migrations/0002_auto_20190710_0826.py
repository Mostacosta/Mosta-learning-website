# Generated by Django 2.2.3 on 2019-07-10 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='right_answer',
            field=models.CharField(choices=[('1', models.CharField(max_length=100)), ('2', models.CharField(max_length=100)), ('3', models.CharField(max_length=100)), ('4', models.CharField(max_length=100))], max_length=20),
        ),
    ]
