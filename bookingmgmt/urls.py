from django.urls import path

from bookingmgmt import views

urlpatterns = [
    path('', views.list_bookings, name = 'list_bookings'),
    path('guests/', views.list_guests, name = 'list_guests'),
]
