from rest_framework import viewsets
from rest_framework import serializers
from ..serializers.product_serializers import ProductSerializers,ModifierSerializers
from apps.users.models import TemporaryUser, Card, CardItem, Order, OrderItem, User
from apps.users.models import Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'full_name']
        read_only_fields = ['id']
