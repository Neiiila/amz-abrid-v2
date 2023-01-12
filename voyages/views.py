from json import dumps
from django.http import HttpResponse
from django.shortcuts import render

from voyages.models import Transport

# Create your views here.

def voyage(request) : 
    qs =  Transport.objects.values('societe', 'type' )
    transports = [{'societe': tran['societe'], 'type': tran['type']} for tran in qs]
    transports = dumps(transports)
    context = {'transports' : transports }
    if( request.method == 'POST') : 
        new_travel = {
            'depart' : request.POST['depart'],
            'destination' : request.POST.get('destination' , False),
            'date_debut' : request.POST['date_debut'],
            'date_fin' : request.POST['date_fin']
        }
    else : 
        return render(request, 'voyages/voyage.html', context)

        
def transport(request) : 
    return render(request , 'voyages/transport.html')