# Generated by Django 5.0.1 on 2024-03-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0009_zonguser_description_alter_zonguser_alias_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='zonguser',
            name='game_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='zonguser',
            name='game_won',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='zonguser',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
