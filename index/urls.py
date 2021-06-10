from django.urls import path

from index import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('hotel', views.hotel, name = 'hotel'),
]
