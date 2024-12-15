from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsUserOrReadOnly(BasePermission):
    """
    Custom permission to check if the user is the owner of an object 
    or allow read-only access for safe methods.
    """

    def has_permission(self, request, view):
        """
        Grant permission if the request method is safe (e.g., GET).
        Write access is checked at the object level.
        """
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated  # Ensure the user is authenticated for non-safe methods.

    def has_object_permission(self, request, view, obj):
        """
        Enforce that the user can access their own object or allow read-only access.
        """
        if request.method in SAFE_METHODS:
            return True  # Allow read-only access for safe methods.
        return obj == request.user  # Allow write access only if the user owns the object.
