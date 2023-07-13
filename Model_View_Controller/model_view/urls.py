from . import views
from django.urls import path

urlpatterns = [
    path('<int:codeNum>',views.sendPrice)
]