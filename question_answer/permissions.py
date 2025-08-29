import logging

from rest_framework.permissions import BasePermission

permission_logger = logging.getLogger("permission")


class IsOwner(BasePermission):
    """Класс разрешения, проверяет, является ли пользователь владельцем по полю user_id."""

    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.user_id.id:
            permission_logger.debug(f"Получен доступ владельцем {request.user.email}")
            return True
        else:
            permission_logger.debug(f"Отказано в доступе к объекту пользователю {request.user.email}")
            return False
