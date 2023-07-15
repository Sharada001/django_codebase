from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('predefined_class',TemplateView.as_view(template_name="main/template_main.html")),
    path('function_based_view',views.function_based_view),
    path('function_based_view/<slug:text>',views.function_based_view_with_path_parameters),
    path('class_based_view',views.class_based_view.as_view()),
    path('class_based_view/<slug:text>',views.class_based_view_with_path_parameters.as_view()),
]