from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class CanAccessResource(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'manager':
            return request.user.department == view.get_object().department
        return False