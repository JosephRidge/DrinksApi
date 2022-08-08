from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):
    # get all drinks 
    # serialize the,
    # return json
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks,many=True)
    return JsonResponse({"Drinks":serializer.data},safe=False )