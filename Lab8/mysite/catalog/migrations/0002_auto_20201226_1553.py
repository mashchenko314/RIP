# Generated by Django 3.1.4 on 2020-12-26 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Processor',
            new_name='Bouquet',
        ),
        migrations.RenameField(
            model_name='description',
            old_name='processor_id',
            new_name='bouquet_id',
        ),
    ]
