from array import array
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.serializers import serialize
import numpy as np 
import pickle
import json
import random    
from APP import *

# from django.db import model



model = pickle.load(open('model.pkl', 'rb'))

def home(request):
    return render(request,"home.html")

# def predict(request):
#     return render(request,"home.html")


# #####################################
# #input user
def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        
    except ValueError:
        try:                                                #BLOCK CAN BE REMOVED
            # Convert it into float
            val = float(input)
            
        except ValueError:
            val=str(input)
    return val
# #####################################
def predict(request):
   l=[]

   age=request.GET['Age']
   bmi=request.GET['BMI']
   cycle=request.GET['Cycle'] 
   weight=request.GET['Weight']
   HairG=request.GET['HairG']
   skin=request.GET['Skin']
   HairL=request.GET['HairL']
   pimples=request.GET['Pimples']
   fast=request.GET['Fast'] 
   regular=request.GET['Regular']

   data=[age,bmi,cycle,weight,HairG,skin,HairL,pimples,fast,regular]

   for x in range(len(data)):
      print("data is:->>>",data[x])


   for x in data:
      z=x
      if isinstance(check_user_input(x),int)== True:                                      #REMOVE CHECK_USER_INPUT()       
         x=z
         print("x is:->>>>",x)
      
      elif isinstance(check_user_input(x),str)== True:
         if x == 'yes':
            x=1
         elif x=='no':
            x=0
         elif x=='regular':
            x=2
         elif x == 'irregular':
            x=4
         else:
            msg="Kindly enter valid input ?"
            return render(request,'home.html',{"msg":msg})
      else:
         msg="Kindly enter valid input ?"
         return render(request,'home.html',{"msg":msg})

      l.append(int(x))
      print("l is:->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",l)

   final_features = [np.array(l)]   
   print("final_fearures:->>>>>>>>",final_features)
   
####################################################
#  model use
   # file="model.pkl"
   # fileobj=open(file,"wb")
   # pickle.dump(l,fileobj)
   # fileobj.close()
   
   
####################################################

   # print("model:***********************************************************",model)
   # print("predict:***********************************************************",predict)
   
   
   prediction = model.predict(final_features)
   
   
   output = round(prediction[0], 2)
   if output == 1:
        output ='Yes you have PCOD, please refer to a gynecologist'   
   elif output == 0:
        output ='No, you don`t have PCOD, Take care of yourself'
   # return render(request,'home.html',prediction_text='Kindly enter valid input? {}'.format(output))
   
   return render(request,'home.html',{"msg":output})
#    ############################################
   

   
   