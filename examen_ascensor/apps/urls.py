from django.urls import  path
from django.conf.urls import url, include
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registrarorden/', views.registrarorden, name='registrarorden'),
    path('logout', views.logout, name='logout'),
   
    
]