# Generated by Django 5.0.1 on 2024-05-04 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0016_zonguser_lastcodesent_zonguser_lastsenttime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zonguser',
            name='token',
        ),
    ]
