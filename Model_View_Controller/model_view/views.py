from django.shortcuts import render
from django.http import HttpResponse
from model_view.models import Food

# Create your views here.
def sendPrice(request,codeNum):
    querySet = Food.objects.filter(code=codeNum).values()
    itemsList = list(querySet)
    if len(itemsList) == 1:
        return HttpResponse("Item : "+itemsList[0]['name']+"    Price : "+str(itemsList[0]['price']) )
    return HttpResponse("Invalid Code !")