from .models import *
from .serializers import *

from rest_framework.permissions import *
from rest_framework.viewsets import ModelViewSet


class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'ADMIN')

class UserViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAdminUser,]