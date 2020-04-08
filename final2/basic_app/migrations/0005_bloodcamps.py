# Generated by Django 3.0.4 on 2020-03-29 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_auto_20200321_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodCamps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Organization_Date', models.DateField()),
                ('Organization_Name', models.CharField(max_length=500)),
                ('Address', models.CharField(max_length=500)),
                ('State', models.CharField(max_length=50)),
                ('District', models.CharField(max_length=50)),
                ('Contact', models.CharField(max_length=10)),
                ('Conducted_by', models.CharField(max_length=100)),
            ],
        ),
    ]
