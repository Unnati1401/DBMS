# Generated by Django 3.0.4 on 2020-03-21 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='Blood_component',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='stock',
            name='Blood_group',
            field=models.CharField(max_length=10),
        ),
    ]
