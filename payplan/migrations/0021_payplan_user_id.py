# Generated by Django 4.2.5 on 2023-12-28 02:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payplan', '0020_flat_alter_volumebonus_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='payplan',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
