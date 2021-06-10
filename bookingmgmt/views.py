from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from bookingmgmt.models import Reservation, Guest

def list_bookings(request):
    bookings = Reservation.objects.all()
    return render(request, 'bookingmgmt/list_bookings.html', {'bookings': bookings})

def list_guests(request):
    guests = Guest.objects.all()
    return render(request, 'bookingmgmt/list_guests.html', {'guests': guests})
