from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
def function_based_view(request):
    context = {'render_name': 'function_based_view'}
    return render(request, "main/template_with_data_rendering.html", context)

def function_based_view_with_path_parameters(request,text):
    context = {'render_name': 'function_based_view', 'text':text}
    return render(request, "main/template_with_more_data_rendering.html", context)


class class_based_view(View):
    def get(self,request):
        context = {'render_name': 'class_based_view'}
        return render(request, "main/template_with_data_rendering.html", context)

class class_based_view_with_path_parameters(View):
    def get(self,request,text):
        context = {'render_name': 'class_based_view', 'text':text}
        return render(request, "main/template_with_more_data_rendering.html", context)