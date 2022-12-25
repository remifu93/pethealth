from rest_framework import permissions


class IsVetUser(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user.is_vet_user)
        return request.user.is_vet_user
