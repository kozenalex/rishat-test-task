# Generated by Django 4.1.7 on 2023-02-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_buy', '0010_rename_tax_order_taxes'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('usd', 'USD'), ('eur', 'EUR')], default='USD', max_length=3),
        ),
    ]
