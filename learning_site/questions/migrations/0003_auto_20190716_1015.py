# Generated by Django 2.2.3 on 2019-07-16 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_answer_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='image',
            field=models.ImageField(blank=True, upload_to='answers'),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, upload_to='questions'),
        ),
    ]
