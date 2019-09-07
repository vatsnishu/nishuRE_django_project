from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'), #pertains to /listings
    path('<int:listing_id>',views.listing, name='listing'), #pertains to listings/id
    path('search',views.search, name='search'), 
]