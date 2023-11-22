# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addresses(models.Model):
    id = models.IntegerField(primary_key=True)
    address_line_1 = models.CharField(blank=True, null=True)
    address_line_2 = models.CharField(blank=True, null=True)
    country = models.CharField(blank=True, null=True)
    state = models.CharField(blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    postal_code = models.CharField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'


class Agents(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
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
    image_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amenities'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Blogs(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blogs'


class ContactInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_info'


class Customers(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Favorites(models.Model):
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    property = models.ForeignKey('Properties', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'favorites'


class Images(models.Model):
    id = models.IntegerField(primary_key=True)
    image_url = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'


class Licenses(models.Model):
    id = models.IntegerField(primary_key=True)
    file = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'licenses'


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
    date_listed = models.DateTimeField(blank=True, null=True, db_comment='Date when the property was listed')

    class Meta:
        managed = False
        db_table = 'properties'


class Reviews(models.Model):
    id = models.IntegerField(primary_key=True)
    property = models.ForeignKey(Properties, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class Transactions(models.Model):
    id = models.IntegerField(primary_key=True)
    price = models.ForeignKey(Prices, models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'
