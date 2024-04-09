from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from . import models

# Create your tests here.
class DataModel:
    Point = ['A','B', 'C', 'D', 'E', 'F']
    
class TaxiModel:
    def taxi_init(n):
        count=models.Taxi.objects.count()
        if count==0:
            for i in range(1,n+1):
                models.Taxi.objects.create(
                    taxi_id=i,
                    customer_id=[""],
                    booking_id=[""],
                    pickup_point=[1],
                    drop_point=[1],
                    pickup_time=[1],
                    drop_time=[1],
                    total_pay=0
                )

        elif count>n:
            for i in range(n,models.Taxi.objects.count()):
                models.Taxi.objects.get(taxi_id=i).delete()

        elif count<n:
            for i in range(count+1, n+1):
                models.Taxi.objects.create(
                    taxi_id=i,
                    customer_id=[],
                    booking_id=[],
                    pickup_point=[1],
                    drop_point=[1],
                    pickup_time=[1],
                    drop_time=[1],
                    total_pay=0
                )
        return True

    def available_taxi(pickup, drop, CPT):
        Taxi_Data = [i for i in models.Taxi.objects.all()]
        CPP = (DataModel.Point.index(pickup)+1)
        CDP = (DataModel.Point.index(drop)+1)
        CDT = CPT+abs(CDP-CPP)

        for Taxi in Taxi_Data:
            flag=0
            Taxi.pickup_point = eval(Taxi.pickup_point)
            Taxi.drop_point = eval(Taxi.drop_point)
            Taxi.pickup_time = eval(Taxi.pickup_time)
            Taxi.drop_time = eval(Taxi.drop_time)
            for i in range(len(Taxi.pickup_point)):
                TPP=Taxi.pickup_point[i]
                TDP=Taxi.drop_point[i]
                TPT=Taxi.pickup_time[i]
                TDT=Taxi.drop_time[i]
                
                if TPP==CPP and TDP==CDP and TPT==CPT and TDT==CDT:
                    flag=1
                    break
                
                elif (TPT>=CDT)==False and (CPT>=TDT)==False:
                    flag=1
                    break
                
                elif (TPT>=CDT) and (CDT+abs(CDP-TPP))>TPT:
                    flag=1
                    break
                
                elif (CPT>=TDT) and TDT+abs(CPP-TDP)>CPT:
                    flag=1
                    break
            if flag==0:return Taxi.taxi_id
            else:
                continue
            
        return 0

    # def schedule(CPP, CDP, CPT, CDT, TPP, TDP, TPT, TDT, taxi_id, BID, customer_id, i):
        Taxi = models.Taxi.objects.get(taxi_id=taxi_id)
        Taxi.pickup_point = eval(Taxi.pickup_point)
        Taxi.drop_point = eval(Taxi.drop_point)
        Taxi.pickup_time = eval(Taxi.pickup_time)
        Taxi.drop_time = eval(Taxi.drop_time)
        Taxi.booking_id = eval(Taxi.booking_id)
        Taxi.pickup_point.remove(TPP)
        Taxi.drop_point.remove(TDP)
        Taxi.pickup_time.remove(TPT)
        Taxi.drop_time.remove(TDT)
        Taxi.total_pay = Taxi.total_pay-(100+(((abs(CDP - CPP)*15)-5)*10))
        Taxi.booking_id.remove(BID)
        Taxi.save()
        
        TaxiModel.update_taxi(taxi_id, BID, CPP, CDP, CPT, CDT)        
        
        models.Booking.objects.get(booking_id=BID).delete()
        
        models.Booking.objects.create(
            taxi_id=taxi_id,
            booking_id=BID,
            customer_id=customer_id,
            pickup_point=CPP,
            drop_point=CDP,
            pickup_time=CPT,
            drop_time=CDT,
            pay=100+(((abs(CDP - CPP)*15)-5)*10)
        )

        TaxiModel.book_taxi(customer_id, CPP, CDP, CPT)

    # def re_schedule(pickup, drop, CPT, customer_id):
        Taxi_Data = [i for i in models.Taxi.objects.all()]
        CPP = (DataModel.Point.index(pickup)+1)
        CDP = (DataModel.Point.index(drop)+1)
        CDT = CPT+abs(CDP-CPP)

        for Taxi in Taxi_Data:
            flag=0
            Taxi.pickup_point = eval(Taxi.pickup_point)
            Taxi.drop_point = eval(Taxi.drop_point)
            Taxi.pickup_time = eval(Taxi.pickup_time)
            Taxi.drop_time = eval(Taxi.drop_time)
            for i in range(len(Taxi.pickup_point)):
                TPP=Taxi.pickup_point[i]
                TDP=Taxi.drop_point[i]
                TPT=Taxi.pickup_time[i]
                TDT=Taxi.drop_time[i]
                BID=Taxi.booking_id[i]
                
                if TPP==CPP and TDP==CDP and TPT==CPT and TDT==CDT:
                    flag=1
                    break
                
                elif (TPT>=CDT)==False and (CPT>=TDT)==False:
                    flag=1
                    break
                elif (TPT>=CDT) and (CDT+abs(CDP-TPP))>TPT:
                    TaxiModel.schedule(CPP, CDP, CPT, CDT, TPP, TDP, TPT, TDT, Taxi.taxi_id, BID, customer_id, i+1)
                elif (CPT>=TDT) and TDT+abs(CPP-TDP)>CPT:
                    flag=1
                    break
            if flag==0:return Taxi.taxi_id
            else:
                continue
            
        return 0

    def update_taxi(taxi_id, booking_id, pickup_point, drop_point, pickup_time, drop_time):
        Taxi_Data = models.Taxi.objects.get(taxi_id=taxi_id)
        
        tpp = eval(Taxi_Data.pickup_point)
        tpp.append(DataModel.Point.index(pickup_point)+1)
        Taxi_Data.pickup_point = str(tpp)
        
        tdp = eval(Taxi_Data.drop_point)
        tdp.append(DataModel.Point.index(drop_point)+1)
        Taxi_Data.drop_point = str(tdp)
                
        tpt = eval(Taxi_Data.pickup_time)
        tpt.append(pickup_time)
        Taxi_Data.pickup_time = str(tpt)
        
        tdt = eval(Taxi_Data.drop_time)
        tdt.append(drop_time)
        Taxi_Data.drop_time = str(tdt)
        
        bid = eval(Taxi_Data.booking_id)
        bid.append(booking_id)
        Taxi_Data.booking_id = str(bid)
        
        Taxi_Data.save()
        
    def book_taxi(customer_id, pickup, drop, pickup_time):
        taxi_id = TaxiModel.available_taxi(pickup, drop, pickup_time)
        if taxi_id == 0:
            return 0
            # return TaxiModel.re_schedule(pickup, drop, pickup_time, customer_id)
        pickup = DataModel.Point.index(pickup) + 1
        drop = DataModel.Point.index(drop) + 1
        drop_time = pickup_time + abs(drop - pickup)
        if drop_time > 24:
            drop_time = drop_time - 24
        pay = 100+(((abs(drop - pickup)*15)-5)*10)
        pickup_point = DataModel.Point[pickup-1]
        drop_point = DataModel.Point[drop-1]
        booking_id = models.Booking.objects.count()+1
        models.Booking.objects.create(
            taxi_id=taxi_id,
            booking_id=booking_id,
            customer_id=customer_id,
            pickup_point=pickup_point,
            drop_point=drop_point,
            pickup_time=pickup_time,
            drop_time=drop_time,
            pay=pay
        )
        TaxiModel.update_taxi(taxi_id, booking_id, pickup_point, drop_point, pickup_time, drop_time)
        return taxi_id
