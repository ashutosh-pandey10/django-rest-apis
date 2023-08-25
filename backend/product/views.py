from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all() # This retrieves only 1 row/item
    serializer_class = ProductSerializer
    # Lookup is done over primary key "pk"

class ProductCreateAPIView(generics.CreateAPIView):
    '''
        Did not understand why the hell is it returning the data even when
        hit as a POST request? Does it have to somthing with how serializers are
        instantiated?
    '''
    # The above question is answered in notes.txt, Q2 in detail. It has to do
    # with how the generics CreateAPIView is implemented
     
    queryset = Product.objects.all() # This retrieves only 1 row/item
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        '''
            This func overrides the default way of how the generic CreateAPIview
            handles the incoming post request data.
        '''
        # serializer.save(user=self.request.user)
        # print(serializer)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")

        if content is None:
            content = title

        serializer.save(content = content)