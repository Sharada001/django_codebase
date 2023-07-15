from django.shortcuts import render

def first_view(request):
    context = {'view_name':'first_view'}
    return render(request,"main/main_template.html",context)

def second_view(request):
    context = {'view_name': 'second_view'}
    return render(request,"main/secondary_template.html",context)