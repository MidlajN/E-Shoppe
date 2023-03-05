from django.urls import path
from E_Cart import views

app_name = 'E_Cart'
urlpatterns = [
    path('add/<int:prod_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_details, name='cart_details'),
    path('remove/<int:prod_id>/', views.cart_remove, name='cart_remove'),
    path('full_remove/<int:prod_id>/', views.full_remove, name='full_remove')
]
