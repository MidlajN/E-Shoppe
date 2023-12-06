from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'categorylist', , basename='CategoryList')

urlpatterns = [
    # path('', include(router.urls)),
    path('products/', views.ProductAPIView.as_view(), name='product-list' ),
    path('products/<int:pk>', views.ProductAPIView.as_view(), name='product' ),
    path('categorylist/', views.CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', views.CategoryDetailAPIView.as_view(), name='category')
]