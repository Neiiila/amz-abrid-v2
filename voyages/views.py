from json import dumps
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from voyages.models import Transport, Hotel

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
    #if( request.method == 'POST') : 
        #new_travel = {
        #    'depart' : request.POST['depart'],
        #    'destination' : request.POST.get('destination' , False),
        #    'date_debut' : request.POST['date_debut'],
        #    'date_fin' : request.POST['date_fin']
        #}
        #return HttpResponse()
    #else : 
    #   
    if( request.method == 'POST') : 
        request.session['depart'] = "Boudinar"
        
    return render(request, 'voyages/voyage.html', context)

        
def transport(request) : 
    return render(request , 'voyages/transport.html')

