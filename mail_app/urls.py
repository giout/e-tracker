from django.urls import path
from . import views

urlpatterns = [
    path('request/', views.reset_link_request, name='reset_link_request'),
    path('sent/', views.reset_link_sent, name='reset_link_sent'),
    path('reset/', views.reset_password, name='reset_password'),
    path('verification/', views.verification, name='verification'),
    path('activation/', views.activation, name='activation'),
]