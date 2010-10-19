from main.models import Trip
from django.db.models import Sum
from django.shortcuts import render_to_response


def graph(request):
    trips = Trip.objects.order_by('when').values('when').annotate(Sum('miles'))
    return render_to_response('main/graph.html',
                              {'trips':trips})
    
