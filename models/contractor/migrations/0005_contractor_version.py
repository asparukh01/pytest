# Generated by Django 4.0.4 on 2022-06-18 07:16

import concurrency.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contractor', '0004_alter_contractor_trust_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='version',
            field=concurrency.fields.AutoIncVersionField(default=0, help_text='record revision number'),
        ),
    ]
