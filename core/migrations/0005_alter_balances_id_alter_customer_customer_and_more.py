# Generated by Django 5.0.2 on 2024-03-27 07:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_balances_id_alter_customer_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balances',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a5923715-bb4b-496a-9a55-303ac408af30'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer',
            field=models.UUIDField(default=uuid.UUID('812b6ab9-b62b-472c-b51b-ed51a3d97af1'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='id',
            field=models.UUIDField(default=uuid.UUID('efa6a714-2c4e-479f-9591-24b42f7738f1'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='id',
            field=models.UUIDField(default=uuid.UUID('99a34af9-8a20-4e12-a87f-c5d45f583128'), primary_key=True, serialize=False),
        ),
    ]
