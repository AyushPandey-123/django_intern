# Generated by Django 3.1.4 on 2020-12-27 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_app', '0004_auto_20201226_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('image_url', models.URLField(max_length=100)),
            ],
        ),
    ]
