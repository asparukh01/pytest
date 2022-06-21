from django.db import models
from django.core.validators import RegexValidator
from .validators import JSONSchemaValidator
from concurrency.fields import AutoIncVersionField


MY_JSON_FIELD_SCHEMA = {
    'schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            'maxLength': 100
        },
        'comment': {
            'type': 'string',
            'maxLength': 150
        }
    },
    'required': ['name'],
    'additionalProperties': False
}


class Contractor(models.Model):
    """Контрагент"""
    version = AutoIncVersionField()
    name = models.CharField(
        max_length=150, null=False, blank=False,
        unique=True, verbose_name='Наименование'
    )
    address = models.CharField(
        max_length=250, null=True, blank=True,
        verbose_name='Адрес'
    )
    IIN_or_BIN = models.CharField(
        null=False, blank=False, max_length=12, unique=True,
        verbose_name='ИИН/БИН', validators=[RegexValidator(r'^\d{12,12}$')]
    )
    IIC = models.CharField(
        max_length=100, null=True, blank=True,
        verbose_name='ИИК'
    )
    bank_name = models.CharField(
        max_length=150, null=True, blank=True,
        verbose_name='Наименование банка'
    )
    BIC = models.CharField(
        max_length=100, null=True, blank=True,
        verbose_name='БИК'
    )
    phone = models.CharField(
        max_length=100, null=False, blank=False,
        verbose_name='Телефон'
    )
    trust_person = models.JSONField(
        null=True, blank=True, default=dict,
        validators=[JSONSchemaValidator(limit_value=MY_JSON_FIELD_SCHEMA)]
    )
    organization = models.ForeignKey(
        'organization.Organization', on_delete=models.PROTECT, null=False, blank=False,
        related_name='contractors', verbose_name='Организация')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Контрагент"
        verbose_name_plural = "Контрагенты"
