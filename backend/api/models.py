from django.db import models
from django.dispatch import receiver
from django.db.models import Avg
from django.db.models.signals import post_save

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class Image(models.Model):
    image = models.ImageField()

    class Meta:
        db_table = 'images'


class Address(models.Model):
    address_line_1 = models.CharField(max_length=255,)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=7, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    @staticmethod
    def create_from_geodata(longitute: float, latitute: float) -> "Address":
        pass
    
    class Meta:
        db_table = 'addresses'



class USER_ROLES(models.TextChoices):
    CUSTOMER = 'Customer'
    AGENT = 'Agent'
    ADMIN = 'Admin'

class UsersManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

        return user

    def create_customer(self, email, password, **extra_fields):
        extra_fields.setdefault('role', USER_ROLES.CUSTOMER)
        return self._create_user(email, password, **extra_fields)

    def create_agent(self, email, password, **extra_fields):
        extra_fields.setdefault('role', USER_ROLES.AGENT)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('role', USER_ROLES.ADMIN)
        return self._create_user(email, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    role = models.CharField(max_length=255, choices=USER_ROLES.choices)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    profile_image = models.ForeignKey(Image, models.SET_NULL, blank=True, null=True)

    objects = UsersManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'users'

    def __str__(self) -> str:
        return self.email




class ContactInfo(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'contact_info'
    
    def __str__(self) -> str:
        return self.name

class Agents(models.Model):
    user = models.OneToOneField(Users, models.DO_NOTHING, null=True)
    contact = models.ForeignKey(ContactInfo, models.SET_NULL, null=True)
    license = models.FileField(default='No License')
    rating = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'agents'

    def __str__(self) -> str:
        return self.user.email

class Customers(models.Model):
    user = models.OneToOneField(Users, models.DO_NOTHING, null=True)
    address = models.ForeignKey(Address, models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'customers'
    
    def __str__(self) -> str:
        return self.user.email

class Reviews(models.Model):
    RATINGS = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    agent = models.ForeignKey(Agents, models.CASCADE)
    customer = models.ForeignKey(Customers, models.DO_NOTHING)
    rating = models.IntegerField(choices=RATINGS)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'reviews'
    
    def __str__(self) -> str:
        return f'{self.agent} - {self.customer}'

@receiver(post_save, sender=Reviews)
def update_agent_rating(sender, instance, **kwargs):
    agent = instance.agent
    agent.rating = Reviews.objects.filter(agent=agent).aggregate(Avg('rating'))['rating__avg']
    agent.save()

class CURRENCY_CHOICES(models.TextChoices):
    USD = 'USD'
    EUR = 'EUR'
    GBP = 'GBP'
    UZS = 'UZS'

class Estate(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True, db_comment='Description of the estate')
    type = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')
    market_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    bedrooms = models.PositiveSmallIntegerField(blank=True, null=True)
    bathrooms = models.PositiveSmallIntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    status = models.BooleanField(default=True)
    agent = models.ForeignKey(Agents, models.DO_NOTHING)
    date_listed = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'estate'

    def __str__(self) -> str:
        return self.title

class Amenities(models.Model):
    estate = models.ForeignKey(Estate, models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey(Image, models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'amenities'

class Contracts(models.Model):
    estate = models.ForeignKey(Estate, models.SET_NULL, null=True)
    agent = models.ForeignKey(Agents, models.SET_NULL, null=True)
    customer = models.ForeignKey(Customers, models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contracts'

    def __str__(self) -> str:
        return f'{self.estate} - {self.customer}'




class Favorites(models.Model):
    customer = models.ForeignKey(Customers, models.CASCADE)
    estate = models.ForeignKey(Estate, models.SET_NULL, null=True)

    class Meta:
        db_table = 'favorites'

    def __str__(self) -> str:
        return f'{self.customer} - {self.estate}'

class Posts(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING)
    title = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        db_table = 'posts'

    def __str__(self) -> str:
        return self.title