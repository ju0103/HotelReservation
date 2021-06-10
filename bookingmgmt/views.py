from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from bookingmgmt.models import Reservation, Guest
from bookingmgmt.forms import BookingForm, GuestForm


def list_bookings(request):
    bookings = Reservation.objects.all()
    return render(request, 'bookingmgmt/list_bookings.html', {'bookings': bookings})

def create_booking(request):
    bookingform = BookingForm(request.POST or None)

    if bookingform.is_valid():
        bookingform.save()
        return redirect('list_bookings')

    return render(request, 'bookingmgmt/booking_form.html', {'bookingform': bookingform})

def update_booking(request, id):
    booking = Reservation.objects.get(id=id)
    bookingform = BookingForm(request.POST or None, instance=booking)

    if bookingform.is_valid():
        bookingform.save()
        return redirect('list_bookings')

    return render(request, 'bookingmgmt/booking_form.html', {'bookingform': bookingform, 'booking': booking})


def list_guests(request):
    guests = Guest.objects.all()
    return render(request, 'bookingmgmt/list_guests.html', {'guests': guests})

def create_guest(request):
    guestform = GuestForm(request.POST or None)

    if guestform.is_valid():
        guestform.save()
        return redirect('list_guests')

    return render(request, 'bookingmgmt/guest_form.html', {'guestform': guestform})

def update_guest(request, id):
    guest = Guest.objects.get(id=id)
    guestform = GuestForm(request.POST or None, instance=guest)

    if guestform.is_valid():
        guestform.save()
        return redirect('list_guests')

    return render(request, 'bookingmgmt/guest_form.html', {'guestform': guestform, 'guest': guest})
