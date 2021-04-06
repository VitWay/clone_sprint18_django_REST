from rest_framework import viewsets
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
