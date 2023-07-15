from django.urls import path
from . import views

app_name = "mainPage"
urlpatterns = [
    path('template', views.render_template, name="template_view"),
]

