# Generated by Django 5.0.2 on 2024-03-27 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_customer_created_at_customer_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balances',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
