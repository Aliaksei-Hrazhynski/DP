# Generated by Django 4.0.2 on 2022-03-03 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=75, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=75, unique=True)),
                ('price', models.IntegerField()),
                ('dish_weight', models.IntegerField()),
                ('flag_promotion', models.BooleanField(blank=True)),
                ('flag_popular', models.BooleanField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cafe.category')),
                ('product', models.ManyToManyField(to='cafe.Product')),
            ],
        ),
    ]
