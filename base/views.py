from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class BasicPermissionViewSet(viewsets.ModelViewSet):
    """
    List with IsAuthenticated
    Rest of endpoints with IsAdminUser
    """

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]