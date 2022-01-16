from rest_framework import permissions

def get_group_names(user):
    return [group.name for group in user.groups.all()]

def is_group_member(user, group_names):
    return any([user.groups.filter(name=group_name) for group_name in group_names])


class IsHROrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return self._has_permission(request)

    def has_object_permission(self, request, view, obj):
        return self._has_permission(request)
    
    def _has_permission(self, request):
        group_names = ['HR']
        user = request.user
        if request.method in permissions.SAFE_METHODS:
            return True
        return user.is_superuser or is_group_member(user, group_names)


class IsUserSelf(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user:
            if user.is_authenticated and request.method in permissions.SAFE_METHODS:
                return True
            return user.is_superuser

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user:
            if user.is_authenticated and request.method in permissions.SAFE_METHODS and user == obj:
                return True
            return user.is_superuser or user == obj

        
class IsResumeManager(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user:
            if user.is_authenticated and request.method in permissions.SAFE_METHODS:
                return True
            return user.is_superuser

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user:
            if user.is_authenticated and request.method in permissions.SAFE_METHODS and user == obj:
                return True
            return user.is_superuser or user == obj