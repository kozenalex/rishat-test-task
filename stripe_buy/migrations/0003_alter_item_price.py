# Generated by Django 4.1.7 on 2023-02-18 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_buy', '0002_order_alter_item_price_ordertoitem_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена'),
        ),
    ]
