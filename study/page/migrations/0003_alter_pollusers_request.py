# Generated by Django 5.0.1 on 2024-03-06 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_rename_reques_pollusers_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollusers',
            name='request',
            field=models.ManyToManyField(blank=True, null=True, to='page.pollusers'),
        ),
    ]