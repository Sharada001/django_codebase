from django.shortcuts import render
from django.utils.html import escape

def first_view(request):
    context = {'view_name':'Main_View'}
    return render(request,"main/main_template.html",context)

def second_view(request):
    context = {'view_name': 'Sub_View'}
    return render(request,"main/secondary_template.html",context)

def view_with_path_parameters(request,text):
    context = {'view_name': 'Param_View', 'text': escape(text)}
    return render(request,"main/third_template.html",context)