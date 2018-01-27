from django.http import HttpResponse
from django.shortcuts import render
from .models import Trips
from trip.forms import TripForm
from django.template import loader
from django.contrib import messages

def index(request):
    form = TripForm()
    context = {'form': form}
    return render(request, 'trip/index.html', context)


def routes(request):
    all_trips = Trips.objects.all()
    context = {'all_trips': all_trips}
    return render(request,'trip/routes.html',context)

def pickRoute(request):
    form = TripForm(request.POST)
    if form.is_valid():
        passengers = request.POST.get('passengers')
        cityA = request.POST.get('cityA')
        cityB = request.POST.get('cityA')
        day_Of_Travel = request.POST.get('day_Of_Travel')
        plausabletrips = getPlausableTripsUsingAStar(cityA,cityB,day_Of_Travel,passengers)
        context = {'plausabletrips': plausabletrips}  #get the plasauble trips and put them in here so you can use them
        #these are all Trip objects
        return render(request, 'trip/routes.html', context)


    else:
        messages.error(request, "Error")
        return HttpResponse("<h1>err <h1>")


    #should hava a no routes found page as well


def getPlausableTripsUsingAStar(cityA,cityB,day_Of_Travel,passengers) : #code for a* using Trips
    #create new Trip objects then return them
    available = Trips.objects.all().filter(city_Of_Departure=cityA) #just a test for filtering nothing to do with your actual part
    #delete it
    return available  #this should actually be returning a list of Trip objects (all the routes with connections. from a to b
    #using Trip.objects.all() (the database with all the routes that we'll have) make a list of  Trip objects using the a*
    #from the the table you'll create
