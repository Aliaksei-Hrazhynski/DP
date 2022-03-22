# Generated by Django 4.0.2 on 2022-03-21 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0011_rename_stock_dish_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images/dish/', verbose_name='Фото блюда'),
        ),
    ]