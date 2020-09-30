# Generated by Django 3.1.1 on 2020-09-16 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_registered', models.DateField(default=datetime.datetime(2020, 9, 16, 21, 51, 43, 496875))),
                ('sku', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=50)),
                ('stocks', models.CharField(max_length=10)),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('image3', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]
