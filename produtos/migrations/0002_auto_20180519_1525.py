# Generated by Django 2.0.5 on 2018-05-19 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produtos',
            old_name='cod_fornecedeor',
            new_name='cod_fornecedor',
        ),
    ]
