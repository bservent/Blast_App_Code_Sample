from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result1/', views.result1, name='result1'),
    path('result2/', views.result2, name='result2'),
]
