from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
    path('read_file/', views.read_file, name='read_file')
]
