# Generated by Django 5.0.1 on 2024-05-03 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0013_zonguser_is42user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zonguser',
            name='is42User',
        ),
        migrations.AddField(
            model_name='zonguser',
            name='isTwoFactorEnabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='zonguser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
