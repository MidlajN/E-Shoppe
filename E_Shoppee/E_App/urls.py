from django.urls import path
from E_App import views

app_name = 'E_App'
urlpatterns = [
    path('', views.AllProdCat, name='AllProdCat'),
    path('<slug:cat_slug>/', views.AllProdCat, name='prod_by_cat'),
    path('<slug:cat_slug>/<slug:product_slug>/', views.ProductDetail, name='ProductDetail'),
    path('/search/', views.SearchResult, name='Search')
]


