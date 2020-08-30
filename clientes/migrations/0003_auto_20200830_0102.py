# Generated by Django 3.1 on 2020-08-30 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_person_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='nome',
        ),
        migrations.AlterField(
            model_name='person',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
