# Generated by Django 4.2.5 on 2023-12-19 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payplan', '0003_volumebump_payplan_volumebonus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volumebump',
            name='bonus',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='volumebump',
            name='unitcount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]