from django.db import models

class Taxi(models.Model):
    taxi_id = models.IntegerField(primary_key = True)
    customer_id = models.TextField(default = [])
    booking_id = models.TextField(default = [])
    pickup_point = models.TextField(default = [1])
    drop_point = models.TextField(default = [1])
    pickup_time = models.TextField(default = [1])
    drop_time = models.TextField(default = [1])
    total_pay = models.IntegerField()

class Booking(models.Model):
    booking_id = models.IntegerField(primary_key = True)
    taxi_id = models.IntegerField()
    customer_id = models.CharField(max_length = 10, default = '0')
    pickup_point = models.CharField(max_length = 1, default = '0')
    drop_point = models.CharField(max_length = 1, default = '0')
    pickup_time = models.IntegerField()
    drop_time = models.IntegerField()
    pay = models.IntegerField()

