from django.contrib import admin
from APP.models import predict_tb


# Register your models here.

class PredictAdmin(admin.ModelAdmin):
    list_display = ("last_period_date", "select_month", "period_days", "Period_Cycle_length", "predict_Data" )


admin.site.register(predict_tb, PredictAdmin)
