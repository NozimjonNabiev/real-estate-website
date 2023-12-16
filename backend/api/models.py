# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agents(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    contact = models.ForeignKey('ContactInfo', models.DO_NOTHING, blank=True, null=True)
    license = models.ForeignKey('Licenses', models.DO_NOTHING, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agents'


class Amenities(models.Model):
    id = models.IntegerField(primary_key=True)
    property = models.ForeignKey('Properties', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey('Images', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amenities'


class ContactInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    users = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField()
    email = models.CharField()
    phone = models.CharField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_info'


class Contracts(models.Model):
    id = models.IntegerField(primary_key=True)
    property = models.ForeignKey('Properties', models.DO_NOTHING, blank=True, null=True)
    agent = models.ForeignKey(Agents, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey('Customers', models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contracts'


class Customers(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Favorites(models.Model):
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    property = models.ForeignKey('Properties', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'favorites'


class Licenses(models.Model):
    id = models.IntegerField(primary_key=True)
    file = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'licenses'


class Posts(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'


class Prices(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prices'


class Properties(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(blank=True, null=True)
    description = models.TextField(blank=True, null=True, db_comment='Description of the property')
    type = models.CharField(blank=True, null=True)
    price = models.ForeignKey(Prices, models.DO_NOTHING, blank=True, null=True)
    market_value = models.ForeignKey(Prices, models.DO_NOTHING, db_column='market_value', related_name='properties_market_value_set', blank=True, null=True)
    address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    agent = models.ForeignKey(Agents, models.DO_NOTHING, blank=True, null=True)
    date_listed = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'properties'


class Reviews(models.Model):
    id = models.IntegerField(primary_key=True)
    agent = models.ForeignKey(Agents, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(unique=True, blank=True, null=True)
    password = models.CharField(blank=True, null=True)
    first_name = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    role = models.CharField(blank=True, null=True)
    profile_image = models.ForeignKey(Images, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
