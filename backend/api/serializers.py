from .models import *

from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.exceptions import ValidationError


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ['__all__']

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['__all__']



class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'password', 'is_staff']
    
    def create(self, validated_data):
        user = Users(
            email=validated_data['email'],
            username=validated_data['username'],
            is_staff=validated_data['is_staff'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class AgentsSerializer(ModelSerializer):
    user = UsersSerializer()

    class Meta:
        model = Agents
        fields = ['__all__']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UsersSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save(role='AGENT')
        account = Agents.objects.create(user=user, **validated_data)
        return account

class CustomersSerializer(ModelSerializer):
    user = UsersSerializer()

    class Meta:
        model = Customers
        fields = ['__all__']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UsersSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save(role='CUSTOMER')
        account = Customers.objects.create(user=user, **validated_data)
        return account


class ContactInfoSerializer(ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['__all__']

class LicensesSerializer(ModelSerializer):
    class Meta:
        model = Licenses
        fields = ['__all__']

class ReviewsSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['__all__']


class EstateSerializer(ModelSerializer):
    class Meta:
        model = Estate
        fields = ['__all__']

class AmenitiesSerializer(ModelSerializer):
    class Meta:
        model = Amenities
        fields = ['__all__']

class ContractsSerializer(ModelSerializer):
    class Meta:
        model = Contracts
        fields = ['__all__']


class FavoritesSerializer(ModelSerializer):
    class Meta:
        model = Favorites
        fields = ['__all__']

class PostsSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = ['__all__']