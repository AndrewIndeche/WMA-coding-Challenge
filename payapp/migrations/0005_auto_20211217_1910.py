# Generated by Django 3.1.2 on 2021-12-17 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0004_auto_20211217_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Authorization', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='account_number',
            new_name='duration',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='account_name',
            new_name='interval',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='card_number',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='cvv',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='tx_ref',
        ),
    ]
