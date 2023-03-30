from django.db import models


# Create your models here.
# create company class

class predict_tb(models.Model):
    last_period_date = models.DateField()
    select_month = models.IntegerField()
    period_days = models.IntegerField()
    Period_Cycle_length = models.IntegerField()
    predict_Data = models.TextField(null=True)





    def __int__(self):
        return self.select_month

    # Last_perioddate=models.AutoField(primary_key=True)
    # name=models.CharField(max_length=50)
    # location=models.CharField(max_length=50)
    # about=models.TextField()
    # type=models.CharField(max_length=100,choices=(('IT','IT'),('Non IT','Non IT'),('phones','phones')))
    # added_date=models.DateTimeField(auto_now=True)
    # active=models.BooleanField(default=True)

    # def __str__(self):
    #     return self.name+'--'+self.location
