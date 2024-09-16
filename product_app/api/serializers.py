from rest_framework import serializers

from products.models import Product
from products.validators import ERROR_MIN_PRICE


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(ERROR_MIN_PRICE)
        return value
