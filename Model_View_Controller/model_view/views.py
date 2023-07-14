from django.shortcuts import render
from django.http import HttpResponse
from model_view.models import Food
from django.utils.html import escape

# Create your views here.
def sendPrice(request,codeNum):
    try :
        obj = Food.objects.get(code=codeNum)
    except Exception as ex:
        return HttpResponse("Invalid Code !")
    return HttpResponse("Item : "+escape(obj.name)+"    Price : "+str(escape(obj.price)) )