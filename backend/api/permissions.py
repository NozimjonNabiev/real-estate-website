from .models import USER_ROLES
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == USER_ROLES.ADMIN)

class IsSelfOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.role == USER_ROLES.ADMIN

class IsAgent(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == USER_ROLES.AGENT)

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == USER_ROLES.ADMIN) or request.method in SAFE_METHODS
    

class IsSelfCustomerOrAgent(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (obj.agent.user == request.user and request.user.role == USER_ROLES.AGENT) or (obj.customer.user == request.user and request.user.role == USER_ROLES.CUSTOMER)
class IsSelfAndCustomer(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (obj.customer.user == request.user and request.user.role == USER_ROLES.CUSTOMER)