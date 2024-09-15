from rest_framework import viewsets, status
from .models import Product, Order, Supplier, OrderItem, Contact, Cart
from .serializers import ProductSerializer, OrderSerializer, SupplierSerializer, ContactSerializer
from django.shortcuts import get_object_or_404
from .utils import send_order_confirmation
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializer

class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart_items = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        product_id = request.data.get('product')
        quantity = request.data.get('quantity', 1)
        product = Product.objects.get(id=product_id)

        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
        cart_item.quantity = quantity
        cart_item.save()

        serializer = CartSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, cart_id):
        try:
            cart_item = Cart.objects.get(id=cart_id, user=request.user)
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

        # Send confirmation email to the customer
        send_order_confirmation(order, request.user.email)

        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ContactView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        contacts = Contact.objects.filter(user=request.user)
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, contact_id):
        try:
            contact = Contact.objects.get(id=contact_id, user=request.user)
            contact.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Contact.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class OrderListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(customer=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)