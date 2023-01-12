from django.urls import path , include
from . import views

urlpatterns = [
    path('voyage', views.voyage, name ='voyage'),
    path('transport', views.transport, name ='transport')
]