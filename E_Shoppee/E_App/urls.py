from django.urls import path, include
from E_App import views

urlpatterns = [
    path('', views.check, name='check')
]
