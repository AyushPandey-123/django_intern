# Generated by Django 3.1.4 on 2020-12-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
