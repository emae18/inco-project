# Generated by Django 4.2.7 on 2023-11-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_roomtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitacion',
            name='src',
            field=models.TextField(default=''),
        ),
    ]
