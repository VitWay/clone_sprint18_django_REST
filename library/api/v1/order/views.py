from rest_framework import viewsets
from .models import Order
from api.v1.authentication.models import CustomUser
from .serializers import OrderSerializer
from rest_framework.exceptions import NotFound
# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer


class OrdersByUserViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().select_related(
        'user'
        ).prefetch_related(
            'book'
        )
    serializer_class = OrderSerializer

    def get_queryset(self, *args, **kwargs):
        user_id = self.kwargs.get("user_pk")
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise NotFound('User with this id does not exist')
        return self.queryset.filter(user=user)