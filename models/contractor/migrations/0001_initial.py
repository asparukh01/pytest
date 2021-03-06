# Generated by Django 4.0.4 on 2022-05-18 15:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from models.contractor import validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='Адрес')),
                ('IIN_or_BIN', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{12,12}$')], verbose_name='ИИН/БИН')),
                ('bank_requisition', models.CharField(blank=True, max_length=250, null=True, verbose_name='Реквизиты банковского счёта')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('trust_person', models.JSONField(blank=True, default=dict, null=True, validators=[validators.JSONSchemaValidator(limit_value={'properties': {'comment': {'maxLength': 150, 'type': 'string'}, 'name': {'maxLength': 100, 'type': 'string'}}, 'required': ['name'], 'schema': 'http://json-schema.org/draft-07/schema#', 'type': 'object'})])),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contractors', to='organization.organization', verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'Контрагент',
                'verbose_name_plural': 'Контрагенты',
            },
        ),
    ]
