from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . import tests, models
from django import template

register = template.Library()

@register.filter
def range_filter(value):
    return range(value)

def bruteforce_testing(request):
    import random
    i=0
    cust_id=1
    while True:
        choice = ('A','B','C','D','E','F')
        cust_id += 1
        pickup = random.choice(choice)
        drop = random.choice(choice)
        pickup_time = random.randint(1, 24)
        if pickup != drop and pickup_time+abs((choice.index(pickup)+1)-(choice.index(drop)+1))<=24:
            i+=1
            tests.TaxiModel.book_taxi(cust_id, pickup, drop, pickup_time)
        if i==11:break
    return HttpResponse("Sucess")

def index(request):
    request.session['taxi_count'] = models.Taxi.objects.count()
    return render(request, 'index.html')

def book_taxi(request):
    customer_id = request.POST.get('customer_id')
    pickup = request.POST.get('pickup_point')
    drop = request.POST.get('drop_point')
    pickup_time = int(request.POST.get('pickup_time'))
    taxi_id = tests.TaxiModel.book_taxi(customer_id, pickup, drop, pickup_time)
    return JsonResponse({'taxi_id':taxi_id,'customer_id':customer_id})

def total_taxi(request):
    total_taxi = request.POST.get('total_taxi')
    tests.TaxiModel.taxi_init(int(total_taxi))
    return JsonResponse({'total_taxi':total_taxi})

def clear_db(request):
    models.Taxi.objects.all().delete()
    models.Booking.objects.all().delete()
    return HttpResponse('Success')

def get_booking_data(request):
    BookingData = models.Booking.objects.all()
    RaxData = {
        'booking':[],
        'total_booking':0
    }
    for i in BookingData:
        RaxData['booking'].append([i.taxi_id, i.customer_id, i.pickup_point, i.drop_point, i.pickup_time, i.drop_time, i.pay])
    RaxData['total_booking'] = len(BookingData)
    return JsonResponse(RaxData)

def get_taxi_count(request):
    return HttpResponse(request.session['taxi_count'])

def get_sorted_booking_data(request):
    search = str(request.POST.get('search')).lower()
    BookingData = models.Booking.objects.all()
    RaxData = {
        'booking':[],
        'total_booking':0
    }
    for i in BookingData:
        if 'taxi' in search and str(i.taxi_id) in search:
            RaxData['booking'].append([i.taxi_id, i.customer_id, i.pickup_point, i.drop_point, i.pickup_time, i.drop_time, i.pay])
            
        elif search == str(i.taxi_id).lower() or search in str(i.customer_id).lower() or search == str(i.pickup_point).lower() or search == str(i.drop_point).lower() or search == str(i.pickup_time).lower() or search == str(i.drop_time).lower() or search == str(i.pay).lower():
            RaxData['booking'].append([i.taxi_id, i.customer_id, i.pickup_point, i.drop_point, i.pickup_time, i.drop_time, i.pay])
    
    RaxData['total_booking'] = len(BookingData)
    return JsonResponse(RaxData)

def selectedtaxi(request):
    search = request.POST.get('taxi_id')
    
    BookingData = models.Booking.objects.all()
    RaxData = {
        'booking':[],
        'total_booking':0
    }
    for i in BookingData:
        if search == str(i.taxi_id) or search=="all":
            RaxData['booking'].append([i.taxi_id, i.customer_id, i.pickup_point, i.drop_point, i.pickup_time, i.drop_time, i.pay])


    RaxData['total_booking'] = len(BookingData)
    return JsonResponse(RaxData)