# Generated by Django 4.2.5 on 2023-12-19 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payplan', '0006_payplan_totalsales'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payplan',
            old_name='frontend',
            new_name='commission',
        ),
        migrations.RemoveField(
            model_name='payplan',
            name='backend',
        ),
    ]
