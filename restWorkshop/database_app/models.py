# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Fires(models.Model):
    year = models.BigIntegerField(db_column='year', blank=True, null=True)
    state = models.TextField(db_column='state', blank=True, null=True)
    month = models.TextField(db_column='month', blank=True, null=True)
    number = models.TextField(db_column='number', blank=True, null=True)  # This field type is a guess.
    date = models.TextField(db_column='date', blank=True, primary_key=True, )

    class Meta:
        managed = False
        db_table = 'Fires'
