from rest_framework.permissions import BasePermission


class OwnerOrStuff(BasePermission):
    """Описать проверку прав доступа для владельца объекта.
Дополнить проверку прав доступа на объект у менеджера (is_staff)."""
    def has_permission(self, request, view):
        if request.user == view.get_object().owner:
            return True
        elif request.user.is_staff:
            return True
        return False
