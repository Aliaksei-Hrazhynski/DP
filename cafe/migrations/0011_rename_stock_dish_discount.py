# Generated by Django 4.0.2 on 2022-03-12 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0010_alter_category_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='stock',
            new_name='discount',
        ),
    ]
