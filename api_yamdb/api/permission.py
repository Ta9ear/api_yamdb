from rest_framework import permissions


class IsAdminModeratorAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_admin:
            return request.user.role == 'admin'
        if request.user.is_moderator:
            return request.user.role == 'moderator'
        if obj.author == request.user:
            return request.user.role == 'author'
        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return request.user.role == 'admin'
        return False
