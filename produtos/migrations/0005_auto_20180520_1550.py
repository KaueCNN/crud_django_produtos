# Generated by Django 2.0.5 on 2018-05-20 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_auto_20180520_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='desc_produto',
            field=models.CharField(max_length=100),
        ),
        migrations.RemoveField(
            model_name='produtos',
            name='fornecedor',
        ),
        migrations.AddField(
            model_name='produtos',
            name='fornecedor',
            field=models.ManyToManyField(blank=True, to='produtos.Fornecedor'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='tipo',
            field=models.CharField(max_length=100),
        ),
    ]
