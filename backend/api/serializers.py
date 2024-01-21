from .models import *

from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.exceptions import ValidationError


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


from django.contrib.auth.hashers import make_password
class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
    
    def create(self, validated_data):
        user = Users.objects._create_user(**validated_data)
        return user
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super(UsersSerializer, self).update(instance, validated_data)
    def partial_update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super(UsersSerializer, self).partial_update(instance, validated_data)

class AgentsSerializer(ModelSerializer):
    user = UsersSerializer()

    class Meta:
        model = Agents
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data.update({'role': USER_ROLES.AGENT})
        user_serializer = UsersSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        account = Agents.objects.create(user=user, **validated_data)
        return account

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)

        if user_data is not None:
            user_data.pop('role', None)
            user_serializer = UsersSerializer(instance.user, data=user_data, partial=True)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()

        return super().update(instance, validated_data)

class CustomersSerializer(ModelSerializer):
    user = UsersSerializer()

    class Meta:
        model = Customers
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data.update({'role': USER_ROLES.CUSTOMER})
        user_serializer = UsersSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        account = Customers.objects.create(user=user, **validated_data)
        return account

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        address_data = validated_data.pop('address', None)

        if user_data is not None:
            user_data.pop('role', None)
            user_serializer = UsersSerializer(instance.user, data=user_data, partial=True)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()

        if address_data is not None:
            address_serializer = AddressSerializer(instance.address, data=address_data, partial=True)
            address_serializer.is_valid(raise_exception=True)
            address_serializer.save()

        return super().update(instance, validated_data)

class ContactInfoSerializer(ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'

class ReviewsSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'


class EstateSerializer(ModelSerializer):
    class Meta:
        model = Estate
        fields = '__all__'

    def create(self, validated_data):
        if validated_data['agent'] == Agents.objects.get(user=self.context['request'].user):
            return super().create(validated_data)
        else:
            raise ValidationError('You are not allowed to add estates to this agent')

class AmenitiesSerializer(ModelSerializer):
    class Meta:
        model = Amenities
        fields = '__all__'

    def create(self, validated_data):
        if validated_data['estate'] in Estate.objects.filter(agent__user=self.context['request'].user):
            return super().create(validated_data)
        else:
            raise ValidationError('You are not allowed to add amenities to this estate')

class ContractsSerializer(ModelSerializer):
    class Meta:
        model = Contracts
        fields = '__all__'

    def create(self, validated_data):
        if validated_data['agent'] == validated_data['estate'].agent and validated_data['agent'] == Agents.objects.get(user=self.context['request'].user):
            return super().create(validated_data)
        else:
            raise ValidationError('You are not allowed to add contracts to this agent with this estate or you are not the agent of estate')


class FavoritesSerializer(ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__'

class PostsSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'