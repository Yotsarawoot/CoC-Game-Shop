# Generated by Django 4.2.4 on 2023-10-20 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_action'),
    ]

    operations = [
        migrations.RenameField(
            model_name='action',
            old_name='action',
            new_name='actionDetail',
        ),
    ]
