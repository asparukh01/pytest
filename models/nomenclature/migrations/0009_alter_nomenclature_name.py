# Generated by Django 4.0.4 on 2022-06-18 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclature', '0008_alter_nomenclature_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomenclature',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Наименование номенклатуры'),
        ),
    ]
