# Generated by Django 3.2.6 on 2021-08-17 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_model'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Model',
            new_name='Comment',
        ),
    ]
