# Generated by Django 4.0.2 on 2022-03-22 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0013_alter_category_options_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ('title', 'id')},
        ),
    ]
