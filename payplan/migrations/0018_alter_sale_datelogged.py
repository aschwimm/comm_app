# Generated by Django 4.2.5 on 2023-12-24 07:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payplan', '0017_alter_sale_datelogged'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='datelogged',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]