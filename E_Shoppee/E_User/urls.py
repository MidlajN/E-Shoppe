from django.urls import path
from E_User import views

app_name = 'E_User'
urlpatterns = [
    path('', views.base_acc, name='Register'),
    path('seller_reg/', views.seller_reg, name='Seller_Reg'),
    path('buyer_reg/', views.buyer_reg, name='Buyer_Reg'),
    path('login/',views.login, name='Login' ),
    path('logout/', views.logout, name='Logout'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('orderstatus/<int:id>/', views.UpdateStatus, name='UpdateStatus')

]
