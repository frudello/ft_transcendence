# Generated by Django 5.0.1 on 2024-03-28 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zonguser',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='static/page/profile_images/'),
        ),
    ]