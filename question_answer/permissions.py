from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.user_id.id:
            return True
        else:
            return False
