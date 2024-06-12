# Generated by Django 5.0.1 on 2024-05-28 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
        ('page', '0019_zonguser_matches'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='reciver',
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='page.zonguser'),
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.ManyToManyField(related_name='chats', to='chat.message')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u1', to='page.zonguser')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u2', to='page.zonguser')),
            ],
        ),
    ]
