# Generated by Django 3.1.1 on 2021-05-04 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_braintree_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='postal_code',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='note',
            field=models.CharField(default='', max_length=256),
        ),
    ]