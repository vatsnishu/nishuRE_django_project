from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'), #pertains to /listings
    path('register',views.register, name='register'), #pertains to listings/id
    path('logout',views.logout, name='logout'), 
    path('dashboard',views.dashboard, name='dashboard')
]