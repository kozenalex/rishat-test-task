# Generated by Django 4.1.7 on 2023-02-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_buy', '0008_tax_order_tax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tax',
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.ManyToManyField(to='stripe_buy.tax'),
        ),
    ]
