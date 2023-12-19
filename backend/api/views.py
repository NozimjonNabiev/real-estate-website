from .models import *
from .serializers import *

from rest_framework.permissions import *
from rest_framework.viewsets import ModelViewSet

# 'create', 'retrieve', 'list', 'destroy', 'update', 'partial_update'

class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'ADMIN')

class IsSelfOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.role == 'ADMIN'

class IsAgent(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'AGENT')

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'ADMIN') or request.method in SAFE_METHODS
    



class UserViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAdmin,]

class AgentsViewSet(ModelViewSet):
    queryset = Agents.objects.all()
    serializer_class = AgentsSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'retrieve']:
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

class LicensesViewSet(ModelViewSet):
    queryset = Licenses.objects.all()
    serializer_class = LicensesSerializer

    def get_permissions(self):
        if self.action in ['list']:
            self.permission_classes = [IsAdmin,]
        else:
            self.permission_classes = [IsSelfOrAdmin,]
        return super(CustomersViewSet, self).get_permissions()


class IsSelfCustomerOrAgent(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (obj.agent.user == request.user and request.user.role == 'AGENT') or (obj.customer.user == request.user and request.user.role == 'CUSTOMER')
class IsSelfAndCustomer(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (obj.customer.user == request.user and request.user.role == 'CUSTOMER')
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