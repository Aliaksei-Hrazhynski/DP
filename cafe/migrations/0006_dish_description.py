# Generated by Django 4.0.2 on 2022-03-03 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0005_alter_dish_flag_novelty'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
