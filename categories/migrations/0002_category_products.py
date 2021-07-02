# Generated by Django 3.2.4 on 2021-06-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_thumbnail'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]