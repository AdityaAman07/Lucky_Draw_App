# Generated by Django 4.2.7 on 2023-11-25 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FLSCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_number', models.IntegerField(unique=True)),
                ('ei_code', models.CharField(max_length=50)),
                ('fls_name', models.CharField(max_length=250)),
                ('rm_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('zone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_number', models.IntegerField(unique=True)),
                ('ei_code', models.CharField(max_length=50)),
                ('partner_name', models.CharField(max_length=250)),
                ('rm_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('zone', models.CharField(max_length=50)),
            ],
        ),
    ]
