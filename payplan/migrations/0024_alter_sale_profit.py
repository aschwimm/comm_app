# Generated by Django 4.2.5 on 2023-12-31 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payplan', '0023_alter_sale_profit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='profit',
            field=models.IntegerField(),
        ),
    ]