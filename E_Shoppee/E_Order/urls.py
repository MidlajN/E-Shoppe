from django.urls import path
from E_Order import views


app_name = 'E_Order'
urlpatterns = [
    path('', views.Order_details, name='order'),
    path('confirm_order/', views.Confirm_order, name='confirm_order')
]