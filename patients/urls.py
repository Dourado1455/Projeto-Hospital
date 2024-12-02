from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('', views.list_patients, name='list_patients'),  
    path('doctors/', views.list_doctors, name='list_doctors'), 
    path('create/', views.create_patient, name='create_patient'),  
]
