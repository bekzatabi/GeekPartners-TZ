# Generated by Django 3.2.8 on 2021-10-31 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
