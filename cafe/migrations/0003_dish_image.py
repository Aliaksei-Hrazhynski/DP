# Generated by Django 4.0.2 on 2022-03-03 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_alter_dish_dish_weight_alter_dish_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='image',
            field=models.ImageField(null=True, upload_to='images/dish/'),
        ),
    ]
