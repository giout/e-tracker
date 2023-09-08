from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('request/', views.reset_link_request, name='reset_link_request'),
    path('sent/', views.reset_link_sent, name='reset_link_sent'),
    path('reset/', views.reset_password, name='reset_password'),
    path('verification/', views.verification, name='verification')
]