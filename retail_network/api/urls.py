from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, SupplierViewSet, ContactView, OrderListView, RegisterView, CartView
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'suppliers', SupplierViewSet, basename='supplier')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
    path('cart/', CartView.as_view(), name='cart'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('contacts/<int:contact_id>/', ContactView.as_view(), name='contact-delete'),
    path('', include(router.urls)),
]

