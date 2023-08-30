from rest_framework import generics, authentication, permissions

from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission
from api.authentication import TokenAuthentication
'''
4.
'''
# Generics with Retrieve ot List handles GET request(retrieves data, as it's name)
# rest Create classes work handles POST requests(updates data)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all() # This retrieves only 1 row/item
    serializer_class = ProductSerializer
    # Lookup is done over primary key "pk"

class ProductListCreateAPIView(generics.ListCreateAPIView):
    '''
    5.
    '''
    # This view class can totally be changed to handle GET requests just by 
    # making it ProductListCreateAPIView and it will return all the 
    # data that is present in the database, since we're creating a query set.
    # 
    # If it were only CreateAPIView, it would have handled only the 
    # GET requests.
    '''
    1.
        Did not understand why the hell is it returning the data even when
        hit as a POST request? Does it have to somthing with how serializers are
        instantiated?
    '''
    '''
    2.
    '''
    # The above question is answered in notes.txt, Q2 in detail. It has to do
    # with how the generics CreateAPIView is implemented
     
    queryset = Product.objects.all() # This retrieves only 1 row/item
    serializer_class = ProductSerializer

    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication
    ]
    # Make sure the in admin view, the user has Staff member check box ticked
    # else, it will not be recognised by the .IsAdminUser flag.
    '''
        8. Custom Permissions
    '''
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    def perform_create(self, serializer):
        '''
        3.
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


class ProductUpdateAPIView(generics.UpdateAPIView):
    '''
        6. UpdateAPIView, allows only PUT methods
    '''
    queryset = Product.objects.all() # This retrieves only 1 row/item
    serializer_class = ProductSerializer
    lookup_field = "pk"
    # Lookup is done over primary key "pk"

    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.content:
            instance.content = instance.title
            # # Try first w/o saving the instance.


class ProductDestroyAPIView(generics.DestroyAPIView):
    '''
        7. DeleteAPIView, allows only DELETE methods
    '''
    queryset = Product.objects.all() # This retrieves only 1 row/item
    serializer_class = ProductSerializer
    lookup_field = "pk"
    # Lookup is done over primary key "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
