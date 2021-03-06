# Generated by Django 3.2.6 on 2021-08-06 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_parent'),
        ('orders', '0002_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.discountcode'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
