# Generated by Django 2.0.5 on 2018-05-20 15:03

from django.db import migrations


class Migration(migrations.Migration):
    
    atomic = False

    dependencies = [
        ('produtos', '0002_auto_20180519_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fornecedor',
            old_name='cod_fornecedor',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='produtos',
            old_name='cod_fornecedor',
            new_name='fornecedor',
        ),
        migrations.RenameField(
            model_name='produtos',
            old_name='cod_produto',
            new_name='id',
        ),
    ]
