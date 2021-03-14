
from django.urls import path, include
from .views import *
urlpatterns = [

    path('', home, name='home' ),
    path('play/', play, name ='play'),
    path('calculate/', calculate, name ='calculate'),
]
