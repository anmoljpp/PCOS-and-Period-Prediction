# from django.shortcuts import render
from rest_framework import viewsets
from .models import predict_tb
from .serializers import PredictSerializers
# from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# create get,post,put,delete method use inbuilt packages
# from rest_framework.decorators import api_view

from django.shortcuts import render
import datetime
from datetime import timedelta


###################################################################################################################

# predict table store data in
class PredictViewSet(viewsets.ModelViewSet):
    queryset = predict_tb.objects.all()
    serializer_class = PredictSerializers

    print("****************serializer_class**************************", serializer_class)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #
    #     serializer.is_valid(raise_exception=True)
    #
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     print("headers Data:->>>>>>", headers)
    #
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


###################################################################################################################


def home(request):
    return render(request, "home.html")


# @api_view(['GET','POST'])

def predict(request):
    # l=[]

    start_date = request.GET['sdate']
    end_date = request.GET['edate']
    period_length = request.GET['cycled']
    period_cycle_duration = request.GET['ppd']

    start_date_int = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = int(end_date)
    period_length_int = int(period_length)
    period_legth_int_second = period_length_int
    period_cycle_duration = int(period_cycle_duration)
    # end_date_int=datetime.datetime.strptime(end_date,"%Y-%m-%d")

    print("start-date:->>>>>", start_date)
    print("data type:->>>>>", type(timedelta(days=period_length_int)))

    all_data = []
    for month in range(1, end_date + 1):
        for day in range(0, period_length_int + 1):
            if period_legth_int_second <= day:
                sum_start_length = start_date_int + timedelta(days=period_cycle_duration)
                all_data.append(sum_start_length)
                # print("sum start lengthhh:->>>>>>>>>>>>>>>>>",sum_start_length)
            else:
                sum_start_length = start_date_int + timedelta(days=day)
                all_data.append(sum_start_length)
                print("sum start length:->>>>>>>>>>>>>>>>>", sum_start_length)
        print("*******************************************************************")
        start_date_int = sum_start_length
    print("All Calendar Details", all_data)

    return render(request, 'home.html')
