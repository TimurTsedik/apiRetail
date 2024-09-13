from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product, Order, Supplier, OrderItem
from .serializers import ProductSerializer, OrderSerializer, SupplierSerializer
from django.shortcuts import get_object_or_404


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        supplier_id = self.request.query_params.get('supplier', None)
        if supplier_id:
            return self.queryset.filter(supplier_id=supplier_id)
        return self.queryset


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        # Create an order
        data = request.data
        order = Order.objects.create(customer=request.user)

        # Add order items
        for item_data in data['items']:
            product = get_object_or_404(Product, id=item_data['product_id'])
            OrderItem.objects.create(order=order, product=product, quantity=item_data['quantity'], price=product.price)

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer