# Generated by Django 3.1 on 2020-08-30 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_auto_20200830_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='observacao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
