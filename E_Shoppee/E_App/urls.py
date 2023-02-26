from django.urls import path, include
from E_App import views

app_name = 'E_App'
urlpatterns = [
    path('', views.AllProdCat, name='AllProdCat'),
    path('<slug:cat_slug>/', views.AllProdCat, name='prod_by_cat'),
]


