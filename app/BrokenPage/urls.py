from django.urls import path
from . import views

urlpatterns = [
    path('', views.BrokenPage, name='broken')
]