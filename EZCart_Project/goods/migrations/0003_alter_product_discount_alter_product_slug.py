# Generated by Django 4.2.11 on 2024-04-05 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_remove_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, null=True, verbose_name='Discount %'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
    ]
