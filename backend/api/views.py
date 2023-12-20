from .models import *
from .serializers import *
from .permissions import *

from rest_framework.viewsets import ModelViewSet


# 'create', 'retrieve', 'list', 'destroy', 'update', 'partial_update'

class UserViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAdmin,]

class AgentsViewSet(ModelViewSet):
    queryset = Agents.objects.all()
    serializer_class = AgentsSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'retrieve']:
            self.permission_classes = [IsSelfOrAdmin,]
        else:
            self.permission_classes = [IsAdmin,]
        return super(AgentsViewSet, self).get_permissions()

class CustomersViewSet(ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'retrieve', 'destroy']:
            self.permission_classes = [IsSelfOrAdmin,]
        elif self.action in ['list']:
            self.permission_classes = [IsAdmin,]
        else:
            self.permission_classes = [AllowAny,]
        return super(CustomersViewSet, self).get_permissions()


class ContactInfoViewSet(ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [AllowAny,]
        else:
            self.permission_classes = [IsAdmin,]
        return super(CustomersViewSet, self).get_permissions()


class ReviewsViewSet(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = [IsSelfCustomerOrAgent, IsAdmin]
        elif self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsSelfAndCustomer, IsAdmin]
        else:
            self.permission_classes = [IsAdmin,]
        return super(CustomersViewSet, self).get_permissions()

class EstateViewSet(ModelViewSet):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAgent, IsAdmin]
        else:
            self.permission_classes = [AllowAny,]
        return super(CustomersViewSet, self).get_permissions()

class AmenitiesViewSet(ModelViewSet):
    queryset = Amenities.objects.all()
    serializer_class = AmenitiesSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAgent, IsAdmin]
        else:
            self.permission_classes = [AllowAny,]
        return super(CustomersViewSet, self).get_permissions()

class ContractsViewSet(ModelViewSet):
    queryset = Contracts.objects.all()
    serializer_class = ContractsSerializer

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsAgent, IsAdmin]
        else:
            self.permission_classes = [IsAdmin]
        return super(CustomersViewSet, self).get_permissions()

class FavoritesViewSet(ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
    permission_classes = [IsSelfAndCustomer, IsAdmin]
    
class PostsViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdmin]
        else:
            self.permission_classes = [AllowAny,]
        return super(CustomersViewSet, self).get_permissions()