# Generated by Django 4.2.6 on 2023-10-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_order_customeraddress_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraddress',
            name='default_address',
            field=models.BooleanField(default=False),
        ),
    ]