# Generated by Django 4.2.7 on 2024-05-10 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_rename_status_position_posi_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='posi_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='posi_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='posi_status',
            new_name='status',
        ),
    ]
