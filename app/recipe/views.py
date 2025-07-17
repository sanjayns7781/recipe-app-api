"""
Views for the recipe APIs.
"""
from rest_framework import viewsets,mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from recipe.serializers import RecipeSerializer,RecipeDetailSerializer,TagSerializer
from core.models import Recipe,Tag


class RecipeViewset(viewsets.ModelViewSet):
    """View for manage recipe APIs"""
    serializer_class = RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retreive recipes for authetnthicated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    def get_serializer_class(self):
        """Return the serializer class for request, maps for two serializer """
        if self.action == 'list':
            return RecipeSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        """"Create a new recipe """
        serializer.save(user=self.request.user)


class TagViewSet(mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,viewsets.GenericViewSet):
    """Manage tags in the database"""
    queryset = Tag.objects.all()
    serializer_class  = TagSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset to authenthicated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
    
    
