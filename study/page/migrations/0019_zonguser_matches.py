# Generated by Django 5.0.1 on 2024-05-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_match_loser_alter_match_winner'),
        ('page', '0018_zonguser_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='zonguser',
            name='matches',
            field=models.ManyToManyField(blank=True, related_name='players', to='game.match'),
        ),
    ]