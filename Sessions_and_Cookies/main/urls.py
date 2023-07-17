from django.urls import path
from . import views

urlpatterns = [
    path('get_view_count', views.get_view_count),
    path('cookies', views.print_cookies),
]
