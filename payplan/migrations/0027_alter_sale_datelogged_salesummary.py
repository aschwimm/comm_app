# Generated by Django 4.2.5 on 2024-01-06 10:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payplan', '0026_usermodel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='datelogged',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.CreateModel(
            name='SaleSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('sale_count', models.IntegerField()),
                ('profit_sum', models.IntegerField()),
                ('profit_avg', models.DecimalField(decimal_places=2, max_digits=100)),
                ('flat_count', models.IntegerField()),
                ('flat_sum', models.IntegerField()),
                ('commission_rate', models.IntegerField()),
                ('commission_earnings', models.IntegerField()),
                ('volume_bonus', models.IntegerField()),
                ('earnings_total', models.DecimalField(decimal_places=2, max_digits=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]