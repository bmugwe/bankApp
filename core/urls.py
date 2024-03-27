from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('balance/', views.getbalances, name='get_balance'),
    path('deposit/', views.postdeposit, name='get_deposit'),
    path('withdraw/', views.postwithdraw, name='get_withdraw'),
    
]