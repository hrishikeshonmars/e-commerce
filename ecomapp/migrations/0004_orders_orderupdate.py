# Generated by Django 5.0 on 2024-03-02 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('name', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=90)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('oid', models.CharField(blank=True, max_length=150)),
                ('amountpaid', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('paymentstatus', models.CharField(blank=True, max_length=20)),
                ('phone', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('update_desc', models.TextField()),
                ('delivered', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomapp.orders')),
            ],
        ),
    ]
