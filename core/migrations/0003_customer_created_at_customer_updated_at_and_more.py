# Generated by Django 5.0.2 on 2024-03-27 05:00

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_balances_id_alter_customer_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 3, 27, 5, 0, 20, 249828, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='balances',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0455e21a-9c38-4a08-b252-58158e91c278'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer',
            field=models.UUIDField(default=uuid.UUID('5a3cf983-deed-416d-9a42-eae77d667260'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='id',
            field=models.UUIDField(default=uuid.UUID('d40685bc-4fdb-4cb5-813b-fa10fbba5a43'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='id',
            field=models.UUIDField(default=uuid.UUID('55ce16cf-dda7-4d62-a651-28824178c833'), primary_key=True, serialize=False),
        ),
    ]
