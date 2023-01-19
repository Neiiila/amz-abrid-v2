
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.voyage, name ='voyage'),
    path('transport', views.transport, name ='transport')
]