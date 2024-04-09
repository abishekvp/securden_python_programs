from . import views

from django.urls import path
from django.urls import path

urlpatterns = [
    # page route
    path('',views.index,name='index'),
    
    # ajax route
    path('total-taxi',views.total_taxi,name='total-taxi'),
    path('book-taxi',views.book_taxi,name='book-taxi'),
    path('clear-db',views.clear_db,name='clear-db'),
    
    path('get-taxi-count',views.get_taxi_count,name='get-taxi-count'),
    path('get-booking-data',views.get_booking_data,name='get-booking-data'),
    path('get-sorted-booking-data',views.get_sorted_booking_data,name='get-sorted-booking-data'),
    path('selectedtaxi',views.selectedtaxi,name='selectedtaxi'),
    
    path('bruteforce_testing',views.bruteforce_testing,name='bruteforce_testing'),   
]


# from django.conf.urls import url
# urlpatterns = [
#     # page route
#     url(r'^',views.index,name='index'),
    
#     # ajax route
#     url(r'^total-taxi/$',views.total_taxi,name='total-taxi'),
#     url(r'^book-taxi/$',views.book_taxi,name='book-taxi'),
#     url(r'^clear-db/$',views.clear_db,name='clear-db'),
    
#     url(r'^get-taxi-count/$',views.get_taxi_count,name='get-taxi-count'),
#     url(r'^get-booking-data/$',views.get_booking_data,name='get-booking-data'),
#     url(r'^get-sorted-booking-data/$',views.get_sorted_booking_data,name='get-sorted-booking-data'),
#     url(r'^selectedtaxi/$',views.selectedtaxi,name='selectedtaxi'),
    
#     url(r'^bruteforce_testing/$',views.bruteforce_testing,name='bruteforce_testing'),   
# ]
