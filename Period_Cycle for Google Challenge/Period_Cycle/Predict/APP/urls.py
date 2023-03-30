from django.contrib import admin
from django.urls import path, include
from .views import PredictViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'predict', PredictViewSet)

urlpatterns = [
    path('', include(router.urls))

]
