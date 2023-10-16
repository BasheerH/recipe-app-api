from rest_framework import viewsets, mixins
from rest_framework.permissions import  IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from core.models import Recipe, Tag
from recipe import serializers

class RecepeViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        """
        Returns the queryset filtered by the current user and ordered by id in descending order.
        """
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """
        Returns the serializer class based on the action performed.
        Parameters:
            self (object): The instance of the class.
        Returns:
            object: The serializer class based on the action performed.
        """
        if self.action == 'list':
            return serializers.RecipeSerializer
        return self.serializer_class

    def perform_create(self, serializer):
            """Create a new recipe."""
            serializer.save(user=self.request.user)

class TagViewSet(mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet,):
    """Manage tags in the database."""

    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        """Return objects for the current authenticated user only."""
        return self.queryset.filter(user=self.request.user).order_by('-name')




