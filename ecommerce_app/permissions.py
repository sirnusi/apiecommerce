from rest_framework import permissions

class ProductOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.owner == request.user
        

class IsOnlyAdminUser(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
        

class IsAuthenticated(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_authenticated)