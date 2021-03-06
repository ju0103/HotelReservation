from django.urls import path

from bookingmgmt import views

urlpatterns = [
    path('', views.list_bookings, name = 'list_bookings'),
    path('newbooking/', views.create_booking, name='add_booking'),
    path('updatebooking/<int:id>/', views.update_booking, name='update_booking'),
    path('deletebooking/<int:id>/', views.delete_booking, name='delete_booking'),

    path('guests/', views.list_guests, name = 'list_guests'),
    path('newguest/', views.create_guest, name='add_guest'),
    path('updateguest/<int:id>/', views.update_guest, name='update_guest'),
    path('deleteguest/<int:id>/', views.delete_guest, name='delete_guest'),

    path('services/', views.list_services, name = 'list_services'),
    path('newservice/', views.add_service, name='add_service'),
    path('updateservice/<int:id>/', views.update_service, name='update_service'),
    path('deleteservice/<int:id>/', views.delete_service, name='delete_service'),

    path('search_guest/', views.search_guest, name='search_guest'),

]
