# Generated by Django 5.0.1 on 2024-03-28 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0011_alter_zonguser_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zonguser',
            name='Description',
        ),
    ]
