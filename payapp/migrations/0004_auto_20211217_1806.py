# Generated by Django 3.1.2 on 2021-12-17 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0003_remove_customer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='fullname',
        ),
    ]
