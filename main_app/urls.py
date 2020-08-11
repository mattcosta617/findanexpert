from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('experts/', views.experts_index, name='experts_index'),
]