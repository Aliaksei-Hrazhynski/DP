# Generated by Django 4.0.2 on 2022-03-12 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0009_alter_dish_options_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',)},
        ),
    ]
