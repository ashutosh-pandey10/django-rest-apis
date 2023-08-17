from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price', # In serializer we can not only directly access model
            'get_discount', # properties, but the functions as well. This makes
            # things much more convenient for us.
        ]