from django.urls import path, include
from api.v1.authentication import views as authentication_views
from api.v1.author import views as author_views
from api.v1.book import views as book_views
from api.v1.order import views as order_views
from rest_framework import routers
from rest_framework_nested import routers as nested_routers

router = routers.DefaultRouter()
router.register('authentication', authentication_views.CustomUserViewSet)
router.register('author', author_views.AuthorViewSet)
router.register('book', book_views.BookViewSet)
router.register('order', order_views.OrderViewSet)

order_router = nested_routers.NestedSimpleRouter(
    router,
    r'authentication',
    lookup='user')

order_router.register(
    r'order',
    order_views.OrdersByUserViewSet,
    basename='user-orders')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(order_router.urls)),
]