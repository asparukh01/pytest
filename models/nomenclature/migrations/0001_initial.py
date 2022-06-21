# Generated by Django 4.0.4 on 2022-05-18 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nomenclature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование номенклатуры')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organization.organization', verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'Номенклатура',
                'verbose_name_plural': 'Номенклатуры',
            },
        ),
    ]
