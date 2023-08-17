from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price', # In serializer we can not only directly access model
            'my_discount', # properties, but the functions as well. This makes
            # things much more convenient for us.
        ]

    '''
    ------------------NEED MORE EXPLANATION ON THIS----------------
    "my_discount" property when initialized, calls for the function 
    get_my_discount()[internal working. If it were instead "discount", 
    it would have called get_discount()].

    This get_my_discount() takes instance of parent model as input
    ie. obj and accesses the method from it.

    Hence to make it work it is important that you save the serializer 
    instance in database. Because that is the only way it can access the 
    model instance of the same query/record.
    '''
    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()