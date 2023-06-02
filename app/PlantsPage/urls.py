from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlantsPage, name='plants'),
]