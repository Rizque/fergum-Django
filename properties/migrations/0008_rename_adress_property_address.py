# Generated by Django 4.1.7 on 2023-05-09 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_remove_property_uuid_alter_property_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='adress',
            new_name='address',
        ),
    ]
