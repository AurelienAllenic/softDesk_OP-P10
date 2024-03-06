from rest_framework.permissions import BasePermission
from api_project.models import Contributor

class IsSuperuserOrReadOnly(BasePermission):
    """
    Permission pour autoriser uniquement les superutilisateurs à effectuer des actions de modification.
    """

    def has_permission(self, request, view):
        # Les superutilisateurs sont autorisés à effectuer n'importe quelle action
        if request.user and request.user.is_superuser:
            return True

        # Les utilisateurs non superutilisateurs ont seulement la permission pour la méthode POST
        return request.method == 'POST'

class IsContributorOrReadOnly(BasePermission):
    """
    Permission pour autoriser les contributeurs à effectuer des actions de modification.
    """

    def has_object_permission(self, request, view, obj):
        # Permettre les méthodes de lecture (GET, HEAD, OPTIONS)
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Vérifier si l'utilisateur actuel est un contributeur de l'objet
        return Contributor.objects.filter(user=request.user, project=obj).exists()

class IsObjectOwnerOrReadOnly(BasePermission):
    """
    Permission pour autoriser le créateur de l'objet à effectuer des actions de modification.
    """

    def has_object_permission(self, request, view, obj):
        # Permettre les méthodes de lecture (GET, HEAD, OPTIONS)
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Vérifier si l'utilisateur actuel est le créateur de l'objet
        return obj.created_by == request.user
