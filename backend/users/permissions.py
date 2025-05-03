from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class CanAccessResource(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'manager':
            return request.user.department == view.get_object().department
        return False
    

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsMentorOrReadOnly(BasePermission):
    """
    Только менторы могут создавать/редактировать, остальные — только читать.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'mentor'

# class IsLearner(BasePermission):
#     """
#     Только для учеников.
#     """
#     def has_permission(self, request, view):
#         return request.user.is_authenticated and request.user.role == 'learner'
