from .serializers import AuthorSerializer
from .models import Author
from rest_framework import viewsets
from rest_framework import permissions


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('surname')
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]