# Generated by Django 3.1.2 on 2021-12-17 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0006_auto_20211218_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('is_premium', 'is_premium'), ('is_not_premium', 'is_not_premium')], default='is_not_premium', help_text='The status of this subscription.', max_length=100),
        ),
    ]