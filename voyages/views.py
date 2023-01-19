from datetime import date
from json import dumps
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from voyages.models import *
from datetime import datetime

# Create your views here.
 
def voyage(request) :
    # Preparation des données de Transport : 
    qs_tr =  Transport.objects.values('societe', 'type' )

    transports = [{'societe': tran['societe'], 'type': tran['type']} for tran in qs_tr]
    transports = dumps(transports)     
    # Preparation des données de Hotel : 
    qs_hot =  Hotel.objects.values('nom', 'localisation' )
    hotels = [{'nom': hot['nom'], 'localisation': hot['localisation']} for hot in qs_hot]
    hotels = dumps(hotels)
    context = {'transports' : transports,
                'hotels' : hotels
     }
    
    if  request.method == 'POST' : 
        depart = request.POST['depart']
        destination = request.POST['destination']
        date_debut  = datetime.strptime(request.POST['date_debut'], "%Y-%m-%d") 
        date_fin = datetime.strptime(request.POST['date_fin'], "%Y-%m-%d") 
        transport = request.POST['transport'] 
        hotel = request.POST['hotel']
        v = Voyage.objects.create(destination = destination, depart = depart)
        
        # if transport != "" : 
        #     transport = None
        # else : 
        #     transport = Transport.objects.filter(societe = transport)[0]

        # if hotel != "" :
        #     hotel = None  
        # else : 
        #     hotel = Hotel.objects.filter(nom = hotel )[0]

        Reservation.objects.create( sejour =  (date_fin - date_debut).days, voyage = v, Transport = None , Hotel = None )
    return render(request, 'voyages/voyage.html',context)

     
def transport(request) : 
    
    return render(request , 'voyages/transport.html')


     
