# Generated by Django 4.2.5 on 2023-12-21 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payplan', '0012_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='salecredit',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='payplan.user'),
            preserve_default=False,
        ),
    ]
