from django.contrib import admin
from django.urls import path
from APP import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('predict/', views.predict),
    path('api/v1/', include('APP.urls')),

]
