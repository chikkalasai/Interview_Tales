# permissions.py

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, OPTIONS for any user
        if request.method in SAFE_METHODS:
            return True
        # Only the owner of the object can update/delete
        return obj.user == request.user
