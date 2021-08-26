from .serializers import OrderSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import Order

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()