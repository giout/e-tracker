from django.urls import path
from . import views

urlpatterns = [
    path('spreadsheet/', views.spreadsheet, name='spreadsheet'), 
    path('chart/', views.chart, name='chart'),
]