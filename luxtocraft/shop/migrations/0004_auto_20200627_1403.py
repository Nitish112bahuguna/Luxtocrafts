# Generated by Django 3.0.6 on 2020-06-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.IntegerField(max_length=111),
        ),
    ]
