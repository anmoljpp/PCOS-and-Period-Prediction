# import datetime
from datetime import timedelta

from rest_framework import serializers
from .models import predict_tb
# from rest_framework import validators


class PredictSerializers(serializers.HyperlinkedModelSerializer):
    # company_id = serializers.ReadOnlyField()


    class Meta:
        model = predict_tb
        fields = ('id', 'last_period_date', 'select_month', 'period_days', 'Period_Cycle_length', 'predict_Data')
        # fields = "__all__"

    def validate(self, data):
        start_date = data['last_period_date']
        end_date = data['select_month']
        period_length = data['period_days']
        period_cycle_duration = data['Period_Cycle_length']

        # End_month = data.get('End_month')




        end_date_int = int(end_date)
        period_length_int = int(period_length)
        period_cycle_duration_int = int(period_cycle_duration)
        period_length_int_second = period_length_int

        # print("******** period_length_int **********", type(period_length_int))
        # print("******** period_cycle_duration_int **********", type(period_cycle_duration_int))
        # print("******** period_length_int timedelta **********", type(timedelta(days=period_length_int)))


        all_data = []
        sum_start_length = start_date
        days = 0

        for month in range(1, end_date_int+1):
            for day in range(0, period_length_int+1):
                if period_length_int_second <= day:
                    sum_start_length = start_date + timedelta(days=period_cycle_duration_int)
                    # print("sum start length (if condition):->>>", sum_start_length)
                    # print("period cycle duration:->>>", period_cycle_duration_int)
                    # print("start date(if condition):->>>", start_date)
                else:
                    sum_start_length = start_date + timedelta(days=days)
                    all_data.append(sum_start_length)
                    start_date = sum_start_length
                    days = 1
                    # print("sum start length (else condition):->>>", sum_start_length)
                    # print("timedelta(days=day) (else):->", timedelta(days=day))

            print("#################################################################")
            start_date = sum_start_length

            data['predict_Data'] = all_data


        return data
