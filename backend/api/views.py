from .models import *
from .serializers import *
from .permissions import *

from rest_framework.views import Response, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# 'create', 'list', 'retrieve', 'update', 'partial_update', 'destroy'

from datetime import datetime
from dateutil.relativedelta import relativedelta


class UserViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAdmin,]

class AgentsViewSet(ModelViewSet):
    queryset = Agents.objects.all()
    serializer_class = AgentsSerializer

    def get_permissions(self):
        if self.action in ['list', 'destroy']:
            self.permission_classes = [IsAdmin,]
        elif self.action in ['update', 'partial_update', 'retrieve']:
            self.permission_classes = [IsSelfOrAdmin,]
        else:
            self.permission_classes = [AllowAny,]
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
        return super(ContactInfoViewSet, self).get_permissions()


class ReviewsViewSet(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = [IsSelfCustomerOrSelfAgentOrAdmin]
        elif self.action in ['create', 'destroy', 'update', 'partial_update']:
            self.permission_classes = [IsSelfAndCustomerOrAdmin]
        else:
            self.permission_classes = [IsAdmin,]
        return super(ReviewsViewSet, self).get_permissions()

class EstateViewSet(ModelViewSet):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'description', 'address__city', 'address__state', 'address__country',]
    ordering_fields = ['price', 'area', 'date_listed',]
    filterset_fields = ['bedrooms', 'bathrooms', 'status', 'agent', 'address__city', 'address__state', 'rent', 'type',]

    def get_permissions(self):
        if self.action in ['destroy']:
            self.permission_classes = [IsAdmin,]
        elif self.action in ['create', 'update', 'partial_update']:
            self.permission_classes = [IsSelfAgentOrAdminForAgent,]
        else:
            self.permission_classes = [AllowAny,]
        return super(EstateViewSet, self).get_permissions()
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         if request.user.role != USER_ROLES.ADMIN:
    #             serializer.save(agent=Agents.objects.get(user=request.user))
    #         else:
    #             serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     if request.user.role != USER_ROLES.ADMIN:
    #         if instance.agent.user != request.user:
    #             return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         if request.user.role != USER_ROLES.ADMIN:
    #             serializer.save(agent=Agents.objects.get(user=request.user))
    #         else:
    #             serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        time = self.request.query_params.get('time', None)

        if time == 'last_month':
            one_month_ago = datetime.now() - relativedelta(months=1)
            queryset = queryset.filter(date_listed__gte=one_month_ago)
        elif time == 'last_week':
            one_week_ago = datetime.now() - relativedelta(weeks=1)
            queryset = queryset.filter(date_listed__gte=one_week_ago)
        elif time == 'today':
            today = datetime.now().date()
            queryset = queryset.filter(date_listed__date=today)

        return queryset



class AmenitiesViewSet(ModelViewSet):
    queryset = Amenities.objects.all()
    serializer_class = AmenitiesSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsSelfAgentOrAdminForEstate,]
        else:
            self.permission_classes = [AllowAny,]
        return super(AmenitiesViewSet, self).get_permissions()

class ContractsViewSet(ModelViewSet):
    queryset = Contracts.objects.all()
    serializer_class = ContractsSerializer

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsSelfAgentOrAdminForAgent,]
        else:
            self.permission_classes = [IsAdmin]
        return super(ContractsViewSet, self).get_permissions()

class FavoritesViewSet(ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
    permission_classes = [IsSelfAndCustomerOrAdmin,]

    def update(self, request, *args, **kwargs):
        pass
    def partial_update(self, request, *args, **kwargs):
        pass
    
class AddressesViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [AllowAny]

class PostsViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdmin]
        else:
            self.permission_classes = [AllowAny,]
        return super(PostsViewSet, self).get_permissions()