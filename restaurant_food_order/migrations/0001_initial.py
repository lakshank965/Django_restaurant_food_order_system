# Generated by Django 4.0.6 on 2022-08-04 09:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desert_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='MainDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_dish', models.CharField(max_length=100)),
                ('main_dish_qty', models.IntegerField()),
                ('side_dish', models.CharField(max_length=100)),
                ('side_dish_qty', models.IntegerField()),
                ('desert', models.CharField(max_length=100)),
                ('desert_qty', models.IntegerField()),
                ('order_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_pay', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SideDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
