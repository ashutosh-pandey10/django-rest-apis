# from django.http import JsonResponse, HttpResponse
from product.models import Product
from product.serializers import ProductSerializer
#  model to dict converts the model instance or query set
#  directly into a dictionary, making things easier for us.

from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

# @api_view(["GET"])
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    -------------------------GET REQUEST--------------------------------
    # The model_to_dict implementation is commented out
    # model_data = Product.objects.all().order_by("?").first()

    instance = Product.objects.all().order_by("?").first()

    data = {}

    if instance:
        # ------------------- w/o model dictionary ------------------------
        # data["id"] = model_data.id
        # data["title"] = model_data.title
        # data["content"] = model_data.content
        # data["price"] = model_data.price

        #  ------------------ Making use of model_to_dict ------------------
        '''
        data = model_to_dict(model_data, fields=['id', 'price', 'title', 'sale_price'])
        
        If the fields parameter in not mentioned, it converts the whole 
        model instance(columns here) to dictionary
        '''
        
        # What am I essentially doing here?
        # calling a model instance --> converting it to python dictionary --> return it as a Json to client!
        # This is exactly what a serializer does.

        # ------------------- Serializer Implementation --------------------
        
        data = ProductSerializer(instance).data
        
    """

    serializer = ProductSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        # This raises detailed exceptions as to which field has encountered
        # the error.
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid" : "Not valid/good data."}, status=400)
    # Removed as it is not used in a rest framework view
    # return JsonResponse(data) 
