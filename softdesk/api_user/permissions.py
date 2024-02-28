from rest_framework.permissions import BasePermission

class IsSuperuserOrReadOnly(BasePermission):
    """
    Permission pour autoriser uniquement les superutilisateurs à effectuer des actions de modification.
    """

    def has_permission(self, request, view):
        # Les superutilisateurs sont autorisés à effectuer n'importe quelle action
        if request.user and request.user.is_superuser:
            return True
        print(request.user and request.user.is_superuser)

        # Les utilisateurs non superutilisateurs ont seulement la permission pour la méthode POST
        return request.method == 'POST'
    
class IsProjectOwnerOrReadOnly(BasePermission):
    """
    Permission pour autoriser uniquement le créateur du projet à effectuer des actions de modification.
    """

    def has_object_permission(self, request, view, obj):
        # Permettre les méthodes de lecture (GET, HEAD, OPTIONS)
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Autoriser seulement le propriétaire du projet à effectuer les modifications
        return obj.created_by == request.user
