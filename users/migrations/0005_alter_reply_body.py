# Generated by Django 4.1.1 on 2022-10-20 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='body',
            field=models.TextField(max_length=999),
        ),
    ]
