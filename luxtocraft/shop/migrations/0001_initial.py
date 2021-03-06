# Generated by Django 3.0.6 on 2020-06-20 11:30

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
                ('product_name', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=250)),
                ('price', models.IntegerField(default=0)),
                ('Images', models.ImageField(upload_to='shop/images')),
                ('published_on', models.DateField()),
            ],
        ),
    ]
