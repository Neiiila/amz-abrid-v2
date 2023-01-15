
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.voyage, name ='voyage'),
    path('transport', views.transport, name ='transport'),
    #url(r'^js_to_django$', views.js_to_django, name='js_to_django')
]