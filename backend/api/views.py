# from django.http import JsonResponse, HttpResponse
from product.models import Product
from django.forms.models import model_to_dict
#  model to dict converts the model instance or query set
#  directly into a dictionary, making things easier for us.

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}

    if model_data:
        # data["id"] = model_data.id
        # data["title"] = model_data.title
        # data["content"] = model_data.content
        # data["price"] = model_data.price

        #  ------------------ Making use of model_to_dict ------------------
        data = model_to_dict(model_data, fields=['id', 'price', 'title'])
        # If the fields parameter in not mentioned, it converts the whole 
        # model instance(columns here) to dictionary
        
        # What am I essentially doing here?
        # calling a model instance --> converting it to python dictionary --> return it as a Json to client!
        # This is exactly what a serializer does.
        
    return Response(data)
    # return JsonResponse(data) #Removed as it is not used in a rest framework view
